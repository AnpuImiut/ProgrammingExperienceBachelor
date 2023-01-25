#include<iostream>
#include<vector>
#include<sstream>
#include<string>
#include<set>
#include<limits>
#include"node.h"

void fillNodes(std::vector<node> &nodes,int nodecount)
{
    nodes.reserve(nodecount);
    for(int j = 0;j<nodecount;++j)
        nodes.emplace_back(j,nodecount);
}
void fillEdges(std::vector<node> &nodes,int connections)
{
    for(int j = 1;j<=connections;++j)
    {
        std::string input;
        int StartNode,EndNode,Distance;
        std::getline(std::cin,input);
        std::istringstream ss(input);
        ss.str(input);
        ss >> StartNode;
        ss >> EndNode;
        ss >> Distance;
        if(StartNode == EndNode)
                continue;
        else
            nodes[StartNode].addEdge(EndNode,Distance);
    }
}
void Mod_Dijakstra(std::vector<node> &nodes)
{
    std::vector<int> distances;
    std::vector<int> visitedCounts;
    std::set<node> Label_new;
    std::set<node> Label_old;
    int source = 0;
    int Min_v;
    int Min_d_New,Min_d_Old;

    distances.resize(nodes.size(),std::numeric_limits<int>::max());
    visitedCounts.resize(nodes.size(),0);
    distances[0] = 0;

    for(int i = 1;i<= 2 * nodes.size();++i)
    {
        visitedCounts[source]++;
        Min_d_Old = std::numeric_limits<int>::max();
        if(visitedCounts[source] > 2 || distances[0] < 0)
        {
            std::cout<< "possible\n";
            return;
        }
        std::vector<edge> tmp = nodes[source].getEdges();
        for(int j = 0;j<tmp.size();++j)
        {
            int EndNode = tmp[j].getNodeId();
            if(distances[EndNode] > distances[source] + tmp[j].getDistance())
            {
                distances[EndNode] = distances[source] + tmp[j].getDistance();
                Label_new.insert(nodes[EndNode]);
                Label_old.erase(nodes[EndNode]);
                Min_d_New = distances[EndNode];
            }
            else
                Min_d_New = std::numeric_limits<int>::max();
            if(Min_d_New < Min_d_Old)
            {
                Min_d_Old = distances[EndNode];
                Min_v = EndNode;
            }
        }
        if(Min_v == source)
        {
            visitedCounts[source]--;
            i--;
        }
        for(auto it : Label_old)
        {
            int nodeId = it.getId();
            if(Min_d_Old > distances[nodeId])
            {
                Min_d_Old = distances[nodeId];
                Min_v = nodeId;
            }
        }
        source = Min_v;
        Label_old.insert(Label_new.begin(),Label_new.end());
        Label_new.clear();
        if(Label_old.empty())
        {
            std::cout<< "not possible\n";
            return;
        }
        Label_old.erase(nodes[source]);
    }
}

int main()
{
    std::string input;
    int testcases;
    std::getline(std::cin,input);
    std::istringstream ss(input);
    ss >> testcases;
    if(testcases == 0)
        return 0;

    for(int i = 1;i<=testcases;++i)
    {
        input.clear();
        ss.clear();
        int nodecount,connections;
        std::vector<node> nodes;
        std::getline(std::cin,input);
        ss.str(input);
        ss >> nodecount;
        ss >> connections;
        if(nodecount == 1 || connections < 2)
        {
            std::cout<< "not possible\n";
            continue;
        }
        fillNodes(nodes,nodecount);
        fillEdges(nodes,connections);
        Mod_Dijakstra(nodes);
    }
}
