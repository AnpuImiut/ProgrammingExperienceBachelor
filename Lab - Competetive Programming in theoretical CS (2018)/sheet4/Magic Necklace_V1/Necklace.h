#ifndef NECKLACE_H_INCLUDED
#define NECKLACE_H_INCLUDED

#include<vector>
#include<cmath>

class Necklace
{
private:
    std::vector<int> perls;
    int first,second;
    int last,lastbefore;
public:
    Necklace(int p);
    ~Necklace();
    void addPearl(int newPearl);
    int getNecklaceSize();

};
#endif // NECKLACE_H_INCLUDED
