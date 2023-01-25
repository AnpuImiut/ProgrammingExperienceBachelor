#ifndef NODE_H_INCLUDED
#define NODE_H_INCLUDED

#include"edge.h"
#include<vector>

class node
{
private:
    int nodeId;
    std::vector<edge> edges;
public:
    node(int id,int nodecount);
    node();
    ~node();
    int getId();
    int getId() const;
    void addEdge(int id,int d);
    std::vector<edge> getEdges();
    bool operator<(const node& arg) const;
};



#endif // NODE_H_INCLUDED
