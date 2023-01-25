#include"DepenCont.h"

DepenCont::DepenCont(int c,std::vector<DepenCont> &n)
{
    num = c;
    numbers = &n;
}

DepenCont::~DepenCont()
{
    dependencies.clear();
}

void DepenCont::addDependence(int arg)
{
    dependencies.push_back(arg);
}

bool DepenCont::operator<(const DepenCont &arg)const
{
    bool found = false;
    if(dependencies.size() > 0)
        found = checkDependence(arg.num);
    if(found)
        return false;
    if(!found && arg.dependencies.size() > 0)
        found = arg.checkDependence(num);
    if(found)
        return true;
    else
        return num < arg.num;
}

int DepenCont::getNum()
{
    return num;
}

bool DepenCont::checkDependence(int n)const
{
    bool found = false;
    for(int i = 0;i<dependencies.size();++i)
    {
        int tmp = dependencies[i];
        if((*numbers)[tmp-1].num == n)
            return true;
        if((*numbers)[tmp-1].dependencies.size() > 0)
            found = (*numbers)[tmp-1].checkDependence(n);
    }
    if(found)
        return true;
    else
        return false;
}

std::vector<int> &DepenCont::getDependen()
{
    return dependencies;
}

