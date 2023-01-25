#include "node.h"

node::node(int i)
{
    id = i;
    cluster = i;
}

node::~node()
{

}

int node::getId()
{
    return id;
}

int node::getCluster()
{
    return cluster;
}

void node::setCluster(int arg)
{
    cluster = arg;
}

std::vector<int> node::getUnionFind()
{
    return UnionFind;
}

void node::addNode(int nodeindex)
{
    UnionFind.push_back(nodeindex);
}

void node::clearUnionFind()
{
    UnionFind.clear();
}
