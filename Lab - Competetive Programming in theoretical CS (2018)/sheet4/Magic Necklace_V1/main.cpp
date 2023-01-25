#include<iostream>
#include"Necklace.h"

int main()
{
    int testcases;
    std::cin>> testcases;
    if(testcases == 0)
        return 0;
    for(int i = 0;i<testcases;++i)
    {
        int perlcount;
        std::cin>> perlcount;
        if(perlcount < 3)
        {
            std::cout<< perlcount << "\n";
            continue;
        }
        else
        {
            Necklace ItsMagic(perlcount);
            for(int j = 0;j<perlcount;++j)
            {
                int tmp;
                std::cin>> tmp;
                ItsMagic.addPearl(tmp);
            }
            std::cout<< ItsMagic.getNecklaceSize() << "\n";
        }
    }
}
