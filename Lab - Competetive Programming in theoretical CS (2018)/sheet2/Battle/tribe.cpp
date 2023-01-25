#include"tribe.h"

tribe::tribe(int anz)
{
    for(int i = 1;i<=anz;++i)
    {
        int number;
        std::cin>> number;
        members.push_back(number);
    }
    std::make_heap(members.begin(),members.end());
}

tribe::~tribe()
{
    members.clear();
}

int tribe::getMax()
{
    std::pop_heap(members.begin(),members.end());
    int result = members.back();
    members.pop_back();
    return result;
}

void tribe::addMember(int arg)
{
    members.push_back(arg);
    std::push_heap(members.begin(),members.end());
}

int tribe::getTribeSize()
{
    return members.size();
}

int tribe::getMemberAt(int i)
{
    return members[i];
}
