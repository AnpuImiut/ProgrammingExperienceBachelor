#include<iostream>
#include<vector>
#include<string>
#include<sstream>
#include<algorithm>

void ausgabe(std::vector<int> arg)
{
    for(int i = 0;i<arg.size();i++)
    {
        std::cout<< arg[i] << " ";
    }
    std::cout<< std::endl;
}


std::vector<int> add(std::vector<int> arg,int input)
{
    bool not_added = true;
    if(arg.size()==0)
    {
        arg.push_back(input);
        return arg;
    }
    for(int i = 0;i<arg.size();i++)
    {
        if(arg[i]>=input)
        {
            arg.insert(arg.begin()+i,input);
            not_added = false;
            break;
        }
    }
    if(not_added)
        arg.push_back(input);
    return arg;
}

int main()
{
    bool run = true;
    std::vector<int> numbers;
    while(run)
    {
        std::string input;
        std::getline(std::cin,input);
        if(input.empty())
            break;
        std::istringstream ss(input);
        int tmp;
        ss>> tmp;
        numbers = add(numbers,tmp);
        if(numbers.size()%2== 0)
        {
            int i = numbers.size();
            int j;
            i /= 2;
            j = i;
            i--;
            std::cout<< (numbers[i] + numbers[j])/2 << std::endl;

        }
        else
        {
            int i = numbers.size() + 1;
            i /= 2;
            i--;
            std::cout<< numbers[i]<< std::endl;
        }

    }
}
