#include"node.h"

node::node(int i)
{
    id = i;
}

node::~node()
{
    edges.clear();
}

void node::addEdge(int e)
{
    edges.push_back(e);
}

std::vector<int> &node::getEdges()
{
    return edges;
}
