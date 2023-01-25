#include "node.h"

node::node(int i)
{
    id = i;
}

node::~node()
{
    parent = nullptr;
}

int node::getId()
{
    return id;
}

node* node::getParent()
{
    return parent;
}

void node::setParent(node* arg)
{
    parent = arg;
}

int node::getNodeCount()
{
    return nodecount;
}

void node::setNodeCount(int arg)
{
    nodecount = arg;
}
