#include "graph.h"

graph::graph(int n)
{
    nodes = n;
    for(int i =0;i<nodes;i++)
    {
        std::set<int> tmp;
        connect.push_back(tmp);
        connect[i].insert(connect[i].begin(),i);
    }
}

graph::~graph()
{
    for(int i = 0;i<connect.size();i++)
    {
        connect[i].clear();
    }
    connect.clear();
}

void graph::addEdge(int s,int e)
{
    s--,e--;
    connect[s].insert(connect[s].begin(),e);
    connect[e].insert(connect[e].begin(),s);
    for(std::set<int>::iterator it = connect[s].begin();it != connect[s].end();it++)
    {
        connect[e].insert(connect[e].begin(),*it);
        for(std::set<int>::iterator j = connect[e].begin();j!=connect[e].end();j++)
        {
            connect[*it].insert(connect[*it].begin(),*j);
        }
    }

    for(std::set<int>::iterator it = connect[e].begin();it != connect[e].end();it++)
    {
        connect[s].insert(connect[s].begin(),*it);
        for(std::set<int>::iterator j = connect[s].begin();j!=connect[s].end();j++)
        {
            connect[*it].insert(connect[*it].begin(),*j);
        }
    }
}

bool graph::connected(int s,int e)
{
    s--,e--;
    if(connect.empty())
        return false;
    if(connect[s].empty())
        return false;
    if(connect[e].empty())
        return false;
    for(std::set<int>::iterator it = connect[s].begin();it!=connect[s].end();it++)
    {
        if(*it == e)
            return true;
    }
    return false;
}

void graph::ausgabe()
{
    for(int i = 0;i<connect.size();i++)
    {
        std::cout<< "Node:"<<i+1 << " is connected to:";
        for(std::set<int>::iterator it =connect[i].begin();it!=connect[i].end();it++)
        {
            std::cout<<(*it)+1 << " ";
        }
        std::cout<< std::endl;
    }
}
