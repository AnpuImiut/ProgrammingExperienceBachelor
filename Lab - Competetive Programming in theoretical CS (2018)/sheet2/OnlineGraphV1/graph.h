#ifndef SET_H_INCLUDED
#define SET_H_INCLUDED

#include<iostream>
#include<vector>
#include<set>

class graph
{
private:
    int nodes = 0;
    std::vector<std::set<int>> connect;

public:
    graph(int n);
    ~graph();
    void addEdge(int s,int e);
    bool connected(int s,int e);
    void ausgabe();
};

#endif // SET_H_INCLUDED
