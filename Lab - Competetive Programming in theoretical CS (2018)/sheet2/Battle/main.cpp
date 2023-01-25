#include <iostream>
#include"tribe.h"
#include<vector>
#include<string>
#include<algorithm>

void fight(std::vector<int> &teamOne,std::vector<int> &teamTwo)
{
    for(int i=0;i<teamOne.size();++i)
    {
        int one = teamOne[i];
        int two = teamTwo[i];
        teamOne[i] -= two;
        teamTwo[i] -= one;
    }
}

std::vector<tribe> testCase(std::istream &istr)
{
    int arenas,tribe1count,tribe2count;
    istr >> arenas;
    istr >> tribe1count;
    istr >> tribe2count;
    tribe one(tribe1count);
    tribe two(tribe2count);

    while(one.getTribeSize()>0 && two.getTribeSize()>0)
    {
        int fightcount = std::min(std::min(one.getTribeSize(),two.getTribeSize()),arenas);
        std::vector<int> tribe1fighters;
        std::vector<int> tribe2fighters;
        for(int i = 1;i<=fightcount;++i)
        {
            tribe1fighters.push_back(one.getMax());
            tribe2fighters.push_back(two.getMax());
        }
        fight(tribe1fighters,tribe2fighters);
        for(int i = 0;i<fightcount;++i)
        {
            if(tribe1fighters[i]>0)
                one.addMember(tribe1fighters[i]);
            if(tribe2fighters[i]>0)
                two.addMember(tribe2fighters[i]);
        }
        tribe1fighters.clear();
        tribe2fighters.clear();
    }
    std::vector<tribe> result;
    result.push_back(one);
    result.push_back(two);
    return result;
}

int main()
{
    int testcaseCount;
    std::cin>> testcaseCount;
    std::vector<tribe> result;
    for(int i = 1;i<=testcaseCount;++i)
    {
        result = testCase(std::cin);
        if(result[0].getTribeSize()== 0 && result[1].getTribeSize() == 0)
        {
            std::cout<< "Both tribes died\n";
        }

        if(result[0].getTribeSize()==0 && result[1].getTribeSize()!= 0)
        {
            std::cout<< "The second tribe survived\n";
            int tribesize = result[1].getTribeSize();
            for(int i = 0;i<tribesize;++i)
                std::cout<< result[1].getMax() << "\n";
        }
        if(result[0].getTribeSize()!=0 && result[1].getTribeSize()== 0)
        {
            std::cout<< "The first tribe survived\n";
            int tribesize = result[0].getTribeSize();
            for(int i = 0;i<tribesize;++i)
                std::cout<< result[0].getMax()<< "\n";
        }
    }
}
