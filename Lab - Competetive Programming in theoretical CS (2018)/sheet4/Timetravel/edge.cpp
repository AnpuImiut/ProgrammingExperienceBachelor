#include"edge.h"

edge::edge(int id,int d)
{
    nodeId = id;
    distance = d;
}

edge::edge()
{
    nodeId = 0;
    distance = 0;
}

edge::~edge()
{

}

int edge::getNodeId()
{
    return nodeId;
}

int edge::getDistance()
{
    return distance;
}
