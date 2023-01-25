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
    if(connected(s,e))
        return;
    s--;e--;
    node* a = &(nodes[s]);
    node* b = &(nodes[e]);
    a = getParent(a);
    b = getParent(b);
    if(a->getNodeCount()<= b->getNodeCount())
    {
        a->setParent(b);
        b->setNodeCount(b->getNodeCount()+a->getNodeCount());
    }
    else
    {
        b->setParent(a);
        a->setNodeCount(a->getNodeCount()+b->getNodeCount());
    }
}

bool graph::connected(int s,int e)
{
    s--;e--;
    int parentA,parentB;
    node* a = &(nodes[s]);
    node* b = &(nodes[e]);
    a = getParent(a);
    b = getParent(b);
    parentA = a->getId();
    parentB = b->getId();
    if(parentA == parentB)
        return true;
    else
        return false;
}

node* graph::getParent(node* arg)
{
    node* tmp = arg;
    while(tmp->getParent()!=nullptr)
        tmp = tmp->getParent();
    return tmp;
}
