#include"CA.h"
//this function just enlarge the buffer or the CMD window so that 84 symbols fit.
void set_console(short hight, short width) {
	HANDLE hCon = GetStdHandle(STD_OUTPUT_HANDLE);
	SMALL_RECT size;
	COORD b_size;

	size.Left = 0;
	size.Top = 0;
	size.Right = width*2;
	size.Bottom = hight*2;
	b_size.X = width+1; //breite+1
	b_size.Y = hight+1; //höhe+1

	SetConsoleWindowInfo(hCon, true, &size);
	SetConsoleScreenBufferSize(hCon, b_size);
}
//non linear function needed to get the right values for the pow function for radius=1
int func1(int i)
{
    if(i==1)
        return 0;
    if(i==0)
        return 1;
    if(i==-1)
        return 2;
}
//non linear function needed to get the right values for the pow function for radius=2
int func2(int i)
{
    if(i==2)
        return 0;
    if(i==1)
        return 1;
    if(i==0)
        return 2;
    if(i==-1)
        return 3;
    if(i==-2)
        return 4;
}
CA::CA():radius(0)
{
    cells.resize(range,0);
    srand(time(0));
}
CA::~CA()
{
    cells.clear();
}
void CA::init()
{
    std::cout<< "Pls enter the radius(1 or 2)...\n";
    std::cin>> radius;
    std::cout<< "Pls enter the rule(0 to " << pow(2,pow(2,2*radius+1))-1 << ")..." << std::endl;
    int tmp;
    std::cin>>tmp;
    setRule(tmp);
    bool seed_mode;
    std::cout<< "Pls enter seed-mode: User(0) or random(1)...\n";
    std::cin>> seed_mode;
    if(!seed_mode)
    {
        std::cout<< "Pls enter the starting bit(2 to 81)...\n";
        std::cin>> tmp;
        UserSeed(tmp);
    }
    else
        randomSeed();
}
void CA::setWindowSettings()
{
    set_console(50,100);
}
void CA::reset()
{
    cells.clear();
    cells.resize(range,0);
    radius=0;
    init();
}
void CA::randomSeed()
{
    for(int i=2;i<82;++i)
        cells[i]=std::rand()%2;
}
void CA::UserSeed(int i)
{
    cells[i]=true;
}
//bitset saves the bit represenation of a integer and make it easily accessable
void CA::setRule(int i)
{
    if(radius==1)
    {
        ruleRad_1=std::bitset<8>(i);
    }
    else
    {
        ruleRad_2=std::bitset<32>(i);
    }
}
void CA::transition()
{
    std::vector<bool> new_arr(range,0);
    for(int i=2;i<82;++i)
    {
        new_arr[i]=apply_rule(i);
    }
    cells=new_arr;
}
void CA::print()
{
    for(auto i:cells)
    {
        if(i)
            std::cout<< char(black_box);
        else
            std::cout<< " ";
    }
    std::cout<< std::endl;
}
void CA::run()
{
    std::cout<< "Welcome to my cellular automata simulator ;)\n";
    init();
    int stop;
    while(true)
    {
        int loops=0;
        std::cout<< "Enter the amount of transitions(int) or reset(0). Exit programm(-1).\n";
        std::cin>> loops;
        if(loops==0)
        {
            reset();
            continue;
        }
        if(loops==-1)
        {
            break;
        }
        for(int i=0;i<loops;++i)
        {
            print();
            transition();
        }
    }
}
//Here i sum up the cell entries where the bit are set with the corrosponding 2^i value and then access the correct entry in the rule array
bool CA::apply_rule(int i)
{
    int sum=0;
    if(radius==1)
    {
        for(int j=+1;j>-2;--j)
        {
            if(cells[i+j])
                sum+=pow(2,func1(j));
        }
        return ruleRad_1[sum];
    }
    else
    {
        for(int j=+2;j>-3;--j)
        {
            if(cells[i+j])
                sum+=pow(2,func2(j));
        }
        return ruleRad_2[sum];
    }
}
