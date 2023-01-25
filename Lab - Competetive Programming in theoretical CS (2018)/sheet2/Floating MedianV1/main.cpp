#include<iostream>
#include<vector>
#include<string>
#include<sstream>
#include<algorithm>

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
        numbers.push_back(tmp);
        std::sort(numbers.begin(),numbers.end());
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
