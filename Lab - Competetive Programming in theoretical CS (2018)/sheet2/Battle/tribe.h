#ifndef TRIBE_H_INCLUDED
#define TRIBE_H_INCLUDED

#include<iostream>
#include<vector>
#include<algorithm>

class tribe
{
private:
    std::vector<int> members;
public:
    tribe(int anz);
    ~tribe();
    int getMax();
    void addMember(int arg);
    int getTribeSize();
    int getMemberAt(int i);

};


#endif // TRIBE_H_INCLUDED
