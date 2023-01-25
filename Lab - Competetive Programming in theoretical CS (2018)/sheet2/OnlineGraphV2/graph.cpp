#include "graph.h"

graph::graph(int n)
{
    for(int i = 0;i<n;i++)
    {
        node tmp(i);
        nodes.push_back(i);
    }
}

graph::~graph()
{
    nodes.clear();
}

void graph::addEdge(int s,int e)
{
    s--;e--;
    nodes[s].addNeighbour(nodes[e]);
    nodes[e].addNeighbour(nodes[s]);
}

bool graph::connected(int s,int e)
{
    s--;e--;
    if(s == e)
        return true;
    if(BFS(s,e));
}

void graph::ausgabe()
{

}

bool graph::BFS(int s,int e)
{
    bool visited[nodes.size()] = {false};
    std::queue<node> work;
    work.push(nodes[s]);
    visited[s] = true;
    while(!work.empty())
    {
        node tmp = work.front();
        work.pop();
        if(tmp.getId() == nodes[e].getId())
            return true;
        std::vector<node> N = tmp.getNeighbour();
        for(int i = 0;i<N.size();i++)
        {
            if(!visited[N[i].getId()])
            {
                visited[N[i].getId()] = true;
                work.push(nodes[N[i].getId()]);
            }
        }
    }
    return false;
}
