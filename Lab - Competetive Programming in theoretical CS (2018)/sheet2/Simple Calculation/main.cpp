#include<sstream>
#include<cstdlib>

#include"BigInt.h"

BigInt calcValues(int n,int k)
{
    BigInt answer("0");
    std::stringstream ss;
    ss<< k;
    std::string b = ss.str();
    BigInt K(b);
    for(int j = 1;j<=n;j++)
    {
        std::stringstream ss;
        ss<< j;
        std::string c = ss.str();
        BigInt J(c);
        BigInt Partial("1");
        for(int c = 1;c<=j;c++)
        {
            Partial = Partial * K;
        }
        Partial = Partial * J;
        answer = answer + Partial;
    }
    return answer;
}

int main()
{
    while(true)
    {
        std::string input;
        int n,k;

        getline(std::cin,input);
        if(input.size() == 0)
            break;
        std::istringstream inputsplit(input);
        inputsplit>> n;
        inputsplit>> k;
        BigInt answer = calcValues(n,k);
        if(answer.getAsString(0) == "0")
            std::cout<< answer.getAsString(0) << std::endl;
        else
            std::cout<< answer.getAsString(1) << std::endl;
    }

//    std::string a,b;
//    std::cin>> a >> b;
//    BigInt A(a);
//    BigInt B(b);
//    BigInt C = A * B;
//    std::cout<< A.getAsString(1) << std::endl;
//    std::cout<< B.getAsString(1) << std::endl;
//    std::cout<< C.getAsString(1) << std::endl;



}
