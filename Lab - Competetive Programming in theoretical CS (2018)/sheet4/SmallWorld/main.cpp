#include<iostream>
#include<map>
#include<string>
#include<queue>

#include"node.h"

void addNodes(int anzNodes,std::vector<node> &nodes)
{
    nodes.reserve(anzNodes);
    for(int i = 1;i <= anzNodes;++i)
        nodes.emplace_back(i);
}

void addEdges(int anzNodes,int anzEdges,std::vector<node> &nodes)
{
    std::map<std::string,int> Map;
    while(anzNodes and anzEdges)
    {
        std::string a,b;
        std::cin>> a >> b;
        if(a[0] == '0' and b[0] == '0')
        {
            anzNodes = 0;
            anzEdges = 0;
        }
        else
        {
            if(Map.find(a) != Map.end() and Map.find(b) != Map.end())
            {
                int node1 = Map[a];
                int node2 = Map[b];
                nodes[node1].addEdge(node2);
                nodes[node2].addEdge(node1);
            }
            else if(Map.find(a) == Map.end() and Map.find(b) != Map.end())
            {
                int mapsize = Map.size();
                Map[a] = mapsize;
                int node1 = Map[a];
                int node2 = Map[b];
                nodes[node1].addEdge(node2);
                nodes[node2].addEdge(node1);
            }
            else if(Map.find(a) != Map.end() and Map.find(b) == Map.end())
            {
                int mapsize = Map.size();
                Map[b] = mapsize;
                int node1 = Map[a];
                int node2 = Map[b];
                nodes[node1].addEdge(node2);
                nodes[node2].addEdge(node1);
            }
            else
            {
                int mapsize = Map.size();
                Map[b] = mapsize;
                mapsize = Map.size();
                Map[a] = mapsize;
                int node1 = Map[a];
                int node2 = Map[b];
                nodes[node1].addEdge(node2);
                nodes[node2].addEdge(node1);
            }
        }
    }
}

bool test_if_connected(std::vector<node> &nodes)
{
    std::vector<bool> visited;
    visited.resize(nodes.size(),false);
    std::queue<int> que;
    que.push(0);
    visited[0] = true;
    while(!que.empty())
    {
        int node = que.front();
        que.pop();
        std::vector<int> edges = nodes[node].getEdges();
        for(auto i : edges)
        {

            if(!visited[i])
            {
                visited[i] = true;
                que.push(i);
            }
        }
    }
    for(auto i : visited)
    {
        if(i == false)
            return false;
    }
    return true;
}

int Init(int anzNodes,int anzEdges,std::vector<node> &nodes)
{
    if(anzNodes == 1 || anzEdges == 0)
        return 0;
    if(anzEdges == anzNodes*(anzNodes - 1))
        return 1;
    addNodes(anzNodes,nodes);
    addEdges(anzNodes,anzEdges,nodes);
    bool connected = test_if_connected(nodes);
    if(connected)
        return 2;
    else
        return -1;
}

int getDiameter(std::vector<node> &nodes)
{
   int diameter = 0;
   int nodesSize = nodes.size();
   for(int i = 0;i<nodesSize;++i)
   {
        //std::cout<< "\nDiamater:" << diameter <<"\nStartNode:" << i << "\n";
        std::vector<bool> visited;
        std::vector<int> depths;
        visited.resize(nodesSize,false);
        depths.resize(nodesSize,0);
        int depth = 0;
        visited[i] = true;
        std::queue<int> que;
        que.push(i);
        while(!que.empty())
        {
            //std::cout<< "QueueSize:" << que.size() << "\n";
            int node = que.front();
            que.pop();
            std::vector<int> edges = nodes[node].getEdges();
            //std::cout<< "Expand Node " << node << "\n";
            for(auto i : edges)
            {
                if(!visited[i])
                {
                    //std::cout<< "Visit Node " << i << ", visited:" << visited[i] << ", depth:"<< depths[i] << "\n";
                    visited[i] = true;
                    que.push(i);
                    depths[i] = depths[node] + 1;
                    if(depths[i] > depth)
                        depth = depths[i];
                }
            }
        }
        if(depth > diameter)
            diameter = depth;
   }
   return diameter;
}

int main()
{
    int anzNodes,anzEdges;
    std::vector<node> nodes;
    std::cin>> anzNodes >> anzEdges;
    if(!anzNodes and !anzEdges)
        return 0;
    int init = Init(anzNodes,anzEdges,nodes);
    switch(init)
    {
    case -1:
        {
            std::cout<< "INFINITY";
            break;
        }
    case 0:
        {
            std::cout<< 0;
            break;
        }
    case 1:
        {
            std::cout<< 1;
            break;
        }
    case 2:
        {
            int answer = getDiameter(nodes);
            std::cout<< answer;
            break;
        }
    }
}

