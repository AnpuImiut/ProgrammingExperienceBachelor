#ifndef CA_H_INCLUDED
#define CA_H_INCLUDED

#include<vector>
#include<windows.h>
#include<time.h>
#include<iostream>
#include<random>
#include<bitset>

#define black_box 219
void set_console(short hight, short width);
int func1(int i);
int func2(int i);

class CA
{
private:

public:
    std::vector<bool> cells;
    const short range=84;
    int radius;
    std::bitset<8> ruleRad_1;
    std::bitset<32> ruleRad_2;

    CA();
    ~CA();
    void init();
    void setWindowSettings();
    void reset();
    void randomSeed();
    void UserSeed(int i);
    void setRule(int i);
    void transition();
    void print();
    void run();
    bool apply_rule(int i);

};


#endif // CA_H_INCLUDED
