#include "node.h"

node::node(int i)
{
    id = i;
}

node::~node()
{
    neighbour.clear();
}

void node::addNeighbour(node arg)
{
    neighbour.push_back(arg);
}

std::vector<node> node::getNeighbour()
{
    return neighbour;
}

int node::getId()
{
    return id;
}
