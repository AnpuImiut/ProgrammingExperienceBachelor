#ifndef NODE_H_INCLUDED
#define NODE_H_INCLUDED

#include<vector>

class node
{
private:
    int id;
    std::vector<int> edges;
public:
    node(int i);
    ~node();
    void addEdge(int e);
    std::vector<int> &getEdges();
};
#endif // NODE_H_INCLUDED
