#ifndef EDGE_H_INCLUDED
#define EDGE_H_INCLUDED

class edge
{
private:
    int nodeId;
    int distance;
public:
    edge();
    edge(int id,int d);
    ~edge();
    int getNodeId();
    int getDistance();
};


#endif // EDGE_H_INCLUDED
