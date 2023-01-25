#ifndef NODE_H_INCLUDED
#define NODE_H_INCLUDED

#include<vector>

class node
{
private:
    int id;
    std::vector<node> neighbour;
public:
    node(int i);
    ~node();
    void addNeighbour(node arg);
    std::vector<node> getNeighbour();
    int getId();

};


#endif // NODE_H_INCLUDED
