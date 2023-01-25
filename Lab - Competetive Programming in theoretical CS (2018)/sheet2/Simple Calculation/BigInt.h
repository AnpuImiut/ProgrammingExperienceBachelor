#ifndef BIGINT_H_INCLUDED
#define BIGINT_H_INCLUDED

#include<string>
#include<vector>
#include<iostream>
#include<math.h>

class BigInt
{
private:
    std::vector<short> number;
public:
    BigInt(std::string input);
    ~BigInt();
    std::string getAsString(bool cut);
    std::vector<short> getData();
    void setData(std::vector<short> arg);
    BigInt operator+(BigInt arg);
    BigInt operator*(BigInt arg);
    void cutZeros();
    void enlarge(int anz);

};

#endif // BIGINT_H_INCLUDED
