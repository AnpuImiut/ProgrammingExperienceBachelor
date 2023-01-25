#ifndef SET_H_INCLUDED
#define SET_H_INCLUDED

#include<iostream>
#include<vector>
#include<queue>
#include"node.h"

class graph
{
private:
    std::vector<node> nodes;
public:
    graph(int n);
    ~graph();
    void addEdge(int s,int e);
    bool connected(int s,int e);
    void ausgabe();
};

#endif // SET_H_INCLUDED
