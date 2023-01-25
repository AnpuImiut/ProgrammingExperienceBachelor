#ifndef NODE_H_INCLUDED
#define NODE_H_INCLUDED

#include<vector>

class node
{
private:
    int id;
    int cluster;
    std::vector<int> UnionFind;
public:
    node(int i);
    ~node();;
    int getId();
    int getCluster();
    void setCluster(int arg);
    std::vector<int> getUnionFind();
    void addNode(int nodeindex);
    void clearUnionFind();

};


#endif // NODE_H_INCLUDED
