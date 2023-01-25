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
    if(nodes[s].getCluster() == nodes[e].getCluster())
        return;
    int ReprS,ReprE;
    ReprS = nodes[s].getCluster();
    ReprE = nodes[e].getCluster();
    if(nodes[ReprS].getUnionFind().size() >= nodes[ReprE].getUnionFind().size())
    {
        nodes[e].setCluster(ReprS);
        nodes[ReprS].addNode(e);
        for(int i =0;i<nodes[ReprE].getUnionFind().size();i++)
        {
            int tmp = (nodes[ReprE].getUnionFind())[i];
            nodes[tmp].setCluster(ReprS);
            nodes[ReprS].addNode(tmp);
        }
        nodes[ReprE].clearUnionFind();
    }
    else
    {
        nodes[s].setCluster(ReprE);
        nodes[ReprE].addNode(s);
        for(int i =0;i<nodes[ReprS].getUnionFind().size();i++)
        {
            int tmp = (nodes[ReprS].getUnionFind())[i];
            nodes[tmp].setCluster(ReprE);
            nodes[ReprE].addNode(tmp);
        }
        nodes[ReprS].clearUnionFind();
    }

}

bool graph::connected(int s,int e)
{
    s--;e--;
    if(nodes[s].getCluster() == nodes[e].getCluster())
        return true;
    else
        return false;
}

void graph::ausgabe()
{

}

