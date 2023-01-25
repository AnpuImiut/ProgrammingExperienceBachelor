#include"Necklace.h"

Necklace::Necklace(int p)
{
    perls.reserve(p);
}

Necklace::~Necklace()
{
    perls.clear();
}

void Necklace::addPearl(int newPearl)
{
    if(perls.size() == 0)
    {
        perls.push_back(newPearl);
        return;
    }
    if(perls.size() == 1)
    {
        if(perls[0] <= newPearl)
        {
            perls.push_back(newPearl);
            return;
        }
        else
        {
            perls.insert(perls.begin(),newPearl);
            return;
        }
    }
    if(perls.size() >= 2)
    {
        if(perls[0] >= newPearl)
        {
            perls.insert(perls.begin(),newPearl);
            return;
        }
        if(perls[1] <= newPearl)
        {
            perls.push_back(newPearl);
            return;
        }
        if(std::abs(perls[1] - newPearl) < std::abs(perls[perls.size() - 2] - newPearl))
        {
            perls[0] = newPearl;
            return;
        }
        else
        {
            perls[perls.size() - 1] = newPearl;
            return;
        }
    }
}

int Necklace::getNecklaceSize()
{
    return perls.size();
}
