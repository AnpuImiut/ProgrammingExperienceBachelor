#include "BigInt.h"

BigInt::BigInt(std::string input)
{
    for(int i = input.size() -1;i>=0;i--)
    {
        number.push_back((int) input[i] - 48);
    }
}

BigInt::~BigInt()
{
    number.clear();
}

std::string BigInt::getAsString(bool cut)
{
    std::string output;
    if(cut)
        cutZeros();
    for(int i = number.size()-1;i>=0;i--)
    {
        output.push_back((char) number[i] + 48);
    }
    return output;
}

std::vector<short> BigInt::getData()
{
    return number;
}

void BigInt::setData(std::vector<short> arg)
{
    number = arg;
}

BigInt BigInt::operator+(BigInt arg)
{
    BigInt answer("0");
    std::vector<short> answerData;
    std::vector<short> argData = arg.getData();
    int Min;
    if(number.size() < argData.size())
    {
        answerData = arg.getData();
        if(argData[argData.size()-1] > 8)
        {
            answerData.resize(argData.size()+1);
        }
        else
            answerData.resize(argData.size());

        Min = number.size();
    }
    else if(number.size() == argData.size())
    {
        answerData = arg.getData();
        if(argData[argData.size()-1] + number[number.size()-1]  > 8)
        {
            answerData.resize(argData.size()+1);
        }
        Min = argData.size();
    }
    else
    {
        answerData = getData();
        if(number[number.size()-1] > 8)
        {
            answerData.resize(number.size()+1);
        }
        Min = argData.size();
    }
    for(int i = 0;i<Min;i++)
    {
        answerData[i] = number[i] + argData[i];
    }
    for(int i = 0;i<answerData.size();i++)
    {
        if(answerData[i] >=10)
        {
            answerData[i+1] = answerData[i+1] + 1;
            answerData[i] %= 10;
        }
    }
    answer.setData(answerData);
    return answer;
}

BigInt BigInt::operator*(BigInt arg)
{
    std::string s("0");
    BigInt answer(s);
    std::vector<short> argData = arg.getData();
    if(number.size()< argData.size())
    {
        for(int i = 0;i<number.size();i++)
        {
            std::string t("0");
            BigInt tmp(t);
            for(int j = 0;j<number[i];j++)
            {
                tmp = tmp + arg;
            }
            if(i>0)
                tmp.enlarge(i);
            answer = answer + tmp;
        }
    }
    else
    {
        for(int i = 0;i<argData.size();i++)
        {
            std::string t("0");
            BigInt tmp(t);
            for(int j = 0;j<argData[i];j++)
            {
                tmp = tmp + *this;
            }
            if(i>0)
                tmp.enlarge(i);
            answer = answer + tmp;
        }
    }
    return answer;
}

void BigInt::cutZeros()
{
    int it = number.size()-1;
    while(true)
    {
        if(number[it--] == 0)
            number.pop_back();
        else
            break;
    }
}

void BigInt::enlarge(int anz)
{
    for(int i = 0;i <anz;i++)
        number.insert(number.begin(),0);
}
