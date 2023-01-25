#include<iostream>
#include<sstream>
#include<string>
#include<cstdlib>
#include<vector>

bool listCompare(std::vector<int> first,std::vector<int> second)
{
    for(int i = 0;i<6;i++)
    {
        if(first[i]<=second[i])
            return true;
        if(second[i]<first[i])
            return false;
    }
    return true;
}

bool listEqual(std::vector<int> first,std::vector<int> second)
{
    for(int i = 0;i<6;i++)
    {
        if(first[i] != second[i])
            return false;
    }
    return true;
}

void mergeTo(std::vector<std::vector<int>> &arg,int low,int middle,int high)
{
    std::vector<std::vector<int>> answer;
    int lowCount = low;
    int HighCount = middle+1;
    while(lowCount<=middle && HighCount<=high)
    {
        if(listCompare(arg[lowCount],arg[HighCount]))
            answer.push_back(arg[lowCount++]);
        else
            answer.push_back(arg[HighCount++]);
    }
    while(lowCount<=middle)
        answer.push_back(arg[lowCount++]);
    while(HighCount<=high)
        answer.push_back(arg[HighCount++]);
    for(int i = low,j=0;i<=high;i++,j++)
        arg[i] = answer[j];
}

void mergeSort(std::vector<std::vector<int>> &arg,int low,int high)
{
    if(high - low<=1)
        return;
    int middle = high - low;
    middle /=2;
    middle+=low;
    mergeSort(arg,low,middle);
    mergeSort(arg,middle+1,high);
    mergeTo(arg,low,middle,high);
}

std::vector<int> lettersToNumbers(std::vector<std::string> arg)
{
    std::vector<int> result;
    for(int i = 0;i<arg.size();i++)
    {
        std::string number;
        int a,b,c,d;
        a = (int)arg[i][0]-50;
        b = (int)arg[i][1]-50;
        c = (int)arg[i][2]-50;
        std::stringstream ss;
        ss<<a;
        number.append(ss.str());
        ss.str("");
        ss<<b;
        number.append(ss.str());
        ss.str("");
        ss<<c;
        number.append(ss.str());
        std::istringstream sh(number);
        sh>>d;
        sh.clear();
        result.push_back(d);
    }
    return result;
}

void GiveOut(std::vector<std::vector<int>> arg)
{
    std::cout<< std::endl;
    for(int i = 0;i<arg.size();i++)
    {
        for(int j=0;j<6;j++)
        {
            std::cout<< arg[i][j] << " ";
        }
        std::cout<< std::endl;
    }
}

void getSorted(std::vector<int> &arg)
{
    for(int c= 0;c<6;c++)
    {
        for(int x = 1;x<6;x++)
        {
            if(arg[x]<arg[x-1])
            {
                int tmp = arg[x-1];
                arg[x-1] = arg[x];
                arg[x] = tmp;
            }
        }
    }
}

void FirstSort(std::vector<std::vector<int>> &arg)
{
    for(int i = 0;i<arg.size();i++)
    {
        getSorted(arg[i]);
    }
}

void SecondSort(std::vector<std::vector<int>> &arg)
{
    mergeSort(arg,0,arg.size()-1);
}

int main()
{
    while(true)
    {
        std::string input;
        getline(std::cin,input);
        int anz = std::atoi(input.c_str());
        if(!anz)
            break;
        std::vector<std::vector<std::string>> chosenV1;
        for(int i = 0;i<anz;i++)
        {
            std::vector<std::string> a;
            getline(std::cin,input);
            std::istringstream inputsplit(input);
            for(int j = 0;j<6;j++)
            {
                std::string tmp;
                inputsplit>> tmp;
                a.push_back(tmp);
            }

            chosenV1.push_back(a);
        }
        std::vector<std::vector<int>> chosenV2;
        for(int n = 0;n<chosenV1.size();n++)
        {
            chosenV2.push_back(lettersToNumbers(chosenV1[n]));
        }
        //GiveOut(chosenV2);
        FirstSort(chosenV2);
        //GiveOut(chosenV2);
        SecondSort(chosenV2);
        //GiveOut(chosenV2);
        int counter[anz+1] = {0};
        int C = 0;
        for(int i = 0;i<chosenV2.size();i++)
        {
            if(chosenV2.size()==1)
            {
                counter[1]++;
                break;
            }
            C++;
            if(i == chosenV2.size()-1)
            {
                if(C!=0)
                {
                    counter[C]++;
                    break;
                }
                else
                {
                    counter[1]++;
                    break;
                }
            }
            if(listEqual(chosenV2[i],chosenV2[i+1]))
                continue;
            else
            {
                counter[C]++;
                C = 0;
            }

        }
        for(int i = anz;i>=1;i--)
        {
            if(counter[i]!= 0)
            {
                std::cout<< counter[i]*i << std::endl;
                break;
            }

        }
    }
}
