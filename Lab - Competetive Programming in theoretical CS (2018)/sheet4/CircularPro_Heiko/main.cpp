#include<iostream>
#include<algorithm>

#include"DepenCont.h"

void fillNumbers(int anz,std::vector<DepenCont> &numbers)
{
    for(int i = 1;i<=anz;++i)
        numbers.emplace_back(i,numbers);
}

void getDependencies(int anz,std::vector<DepenCont> &numbers)
{
    for(int i = 1;i<=anz;++i)
    {
        int s,e;
        std::cin>> s >> e;
        numbers[e-1].addDependence(s);
    }
}

void ausgabe(std::vector<DepenCont> &numbers)
{
    for(auto i : numbers)
    {
        std::cout<< i.getNum() << " ";
    }
    std::cout<< "\n";
}

int main()
{
    int n,m;
    std::cin>> n >> m;
    while(n and m)
    {
        std::vector<DepenCont> numbers;
        numbers.reserve(n);
        fillNumbers(n,numbers);
        getDependencies(m,numbers);
        std::sort(numbers.begin(),numbers.end());
        ausgabe(numbers);
        std::cin>> n >> m;
    }
}
