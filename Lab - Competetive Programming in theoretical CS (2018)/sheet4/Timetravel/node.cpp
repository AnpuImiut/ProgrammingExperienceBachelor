#include"node.h"

node::node(int id,int nodecount)
{
    nodeId = id;
    edges.reserve(nodecount);
}

node::node()
{
    nodeId = 0;
}

node::~node()
{
    edges.clear();
}

int node::getId()
{
    return nodeId;
}

int node::getId() const
{
    return nodeId;
}

void node::addEdge(int id,int d)
{
    edges.emplace_back(id,d);
}

std::vector<edge> node::getEdges()
{
    return edges;
}

bool node::operator<(const node& arg) const
{
    return nodeId < arg.nodeId;
}
