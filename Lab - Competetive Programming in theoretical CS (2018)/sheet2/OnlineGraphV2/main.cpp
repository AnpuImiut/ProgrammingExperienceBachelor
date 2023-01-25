#include "graph.h"
#include<string>
#include<sstream>
#include<cstdlib>

int main()
{
    std::string input;
    getline(std::cin,input);
    int anz = std::atoi(input.c_str());
    if(!anz)
        return 0;
    for(int i = 1;i<=anz;i++)
    {
        int n,events,counter,querycount;
        counter = 0;
        querycount = 0;
        getline(std::cin,input);
        std::istringstream inputsplit(input);
        inputsplit>> n;
        inputsplit>> events;
        graph A(n);
        for(int j = 1;j<=events;j++)
        {
            inputsplit.clear();
            char mode;
            int s,e;
            getline(std::cin,input);
            inputsplit.str(input);
            inputsplit>> mode;
            inputsplit>> s;
            inputsplit>> e;
            if(mode == 'q')
            {
                querycount++;
                if(A.connected(s,e))
                {
                    counter++;

                }
            }
            else
            {
                A.addEdge(s,e);
                //A.ausgabe();
            }
        }
        std::cout<< counter << " " << querycount-counter << std::endl;
    }
}
