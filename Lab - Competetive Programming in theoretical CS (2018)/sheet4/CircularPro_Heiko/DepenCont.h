#ifndef DEPENCONT_H_INCLUDED
#define DEPENCONT_H_INCLUDED

#include<iostream>
#include<vector>

class DepenCont
{
private:
    int num;
    std::vector<int> dependencies;
    std::vector<DepenCont> *numbers;
public:
    DepenCont(int c,std::vector<DepenCont> &n);
    ~DepenCont();
    void addDependence(int arg);
    bool operator<(const DepenCont &arg)const;
    int getNum();
    bool checkDependence(int n)const;
    std::vector<int> &getDependen();
    void ausgabeNumbers()const;
};


#endif // DEPENCONT_H_INCLUDED
