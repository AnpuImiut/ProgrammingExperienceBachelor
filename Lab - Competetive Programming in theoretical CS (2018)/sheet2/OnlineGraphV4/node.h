#ifndef NODE_H_INCLUDED
#define NODE_H_INCLUDED

#include<vector>

class node
{
private:
    int id;
    int nodecount = 1;
    node *parent = nullptr;
public:
    node(int i);
    ~node();;
    int getId();
    node* getParent();
    void setParent(node* arg);
    int getNodeCount();
    void setNodeCount(int arg);

};


#endif // NODE_H_INCLUDED
