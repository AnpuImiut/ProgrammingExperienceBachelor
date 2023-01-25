#include<iostream>
#include<vector>
#include<string>
#include<stdlib.h>
#include<sstream>
#include<iomanip>
#include<limits>
#include<math.h>

struct Point2D
{
    int x;
    int y;
};

struct Point2Ddouble
{
    double x;
    double y;
};

struct NSAanswer
{
    double value;
    int seg;
    bool Class;
};

void INPUT(Point2D &a,std::vector<Point2D> &Pval,int &segments,std::string input)
{
    a.x = atoi(input.c_str());
    input.clear();
    std::getline(std::cin,input);
    a.y = atoi(input.c_str());
    input.clear();
    std::getline(std::cin,input);
    segments = atoi(input.c_str());
    if(!segments)
        return;
    input.clear();
    Pval.reserve(segments+1);
    for(int i = 1;i<=segments+1;++i)
    {
        Point2D tmp;
        std::getline(std::cin,input);
        tmp.x = atoi(input.c_str());
        input.clear();
        std::getline(std::cin,input);
        tmp.y = atoi(input.c_str());
        input.clear();
        Pval.push_back(tmp);
    }
}

bool classify(Point2D &A,Point2D &P1,Point2D &P2)
{
    Point2D P1_A;
    Point2D P2_A;
    Point2D P1_P2;
    int sc1,sc2;
    P1_A.x = A.x - P1.x;
    P1_A.y = A.y - P1.y;
    P2_A.x = A.x - P2.x;
    P2_A.y = A.y - P2.y;
    P1_P2.x = P2.x - P1.x;
    P1_P2.y = P2.y - P1.y;
    sc1 = P1_A.x*P1_P2.x + P1_A.y*P1_P2.y;
    sc2 = P2_A.x*P1_P2.x + P2_A.y*P1_P2.y;
    if(sc1*sc2 < 0)
        return 1;
    else
        return 0;
}

NSAanswer nearestSegmentAltitude(Point2D &A,std::vector<Point2D> &Pval)
{
    NSAanswer output;
    output.value = std::numeric_limits<double>::max();
    for(int i = 0;i< Pval.size() - 1;++i)
    {
        if(classify(A,Pval[i],Pval[i+1]))
        {
            double a,b,c,s,tmp;
            a = sqrt((Pval[i].x - Pval[i+1].x)*(Pval[i].x - Pval[i+1].x) + (Pval[i].y - Pval[i+1].y)*(Pval[i].y - Pval[i+1].y));
            b = sqrt((Pval[i].x - A.x)*(Pval[i].x - A.x) + (Pval[i].y - A.y)*(Pval[i].y - A.y));
            c = sqrt((Pval[i+1].x - A.x)*(Pval[i+1].x - A.x) + (Pval[i+1].y - A.y)*(Pval[i+1].y - A.y));
            s = 0.5 * (a+b+c);
            tmp = (2.0/a) * sqrt(s*(s-a)*(s-b)*(s-c));
            //std::cout<< "i: " << i << " d: " << tmp << "\n";
            if(fabs(tmp-output.value) < 1E-5 || tmp <= output.value)
            {
                //std::cout<< "new i: " << i << "\n";
                output.value = tmp;
                output.seg = i;
                output.Class = 1;
            }
            else
            {
                //std::cout<< tmp << " is bigger than " << output.value << "\n";
            }

        }
        else
        {
            double tmp1,tmp2;
            tmp1 = sqrt((Pval[i].x - A.x)*(Pval[i].x - A.x) + (Pval[i].y - A.y)*(Pval[i].y - A.y));
            tmp2 = sqrt((Pval[i+1].x - A.x)*(Pval[i+1].x - A.x) + (Pval[i+1].y - A.y)*(Pval[i+1].y - A.y));
            if(tmp1 < tmp2)
            {
                if(fabs(tmp1-output.value) < 1E-5 || tmp1 <= output.value)
                {
                    //std::cout<< "new i: " << i << "\n";
                    output.value = tmp1;
                    output.seg = i;
                    output.Class = 0;
                }
                else
                {
                    //std::cout<< tmp << " is bigger than " << output.value << "\n";
                }

            }
            else
            {
                if(fabs(tmp2-output.value) < 1E-5 || tmp2 <= output.value)
                {
                    //std::cout<< "new i: " << i << "\n";
                    output.value = tmp2;
                    output.seg = i+1;
                    output.Class = 0;
                }
                else
                {
                    //std::cout<< tmp << " is bigger than " << output.value << "\n";
                }

            }
        }
    }
    //std::cout<< "Output: " << output.seg << "\n";
    return output;
}

Point2Ddouble calcPoint(Point2D &A,std::vector<Point2D> &Pval,NSAanswer &nearestSegment)
{
    Point2Ddouble output;
    Point2Ddouble vec;
    int i = nearestSegment.seg;
    double b,r,vecNorm;
    vec.x = Pval[i+1].x - Pval[i].x;
    vec.y = Pval[i+1].y - Pval[i].y;
    b = sqrt((Pval[i].x - A.x)*(Pval[i].x - A.x) + (Pval[i].y - A.y)*(Pval[i].y - A.y));
    r = sqrt(b*b - nearestSegment.value*nearestSegment.value);
    vecNorm = sqrt(vec.x*vec.x+vec.y*vec.y);
    vec.x = (r/vecNorm) * vec.x;
    vec.y = (r/vecNorm) * vec.y;
    output.x = Pval[i].x + vec.x;
    output.y = Pval[i].y + vec.y;
    return output;
}

int main()
{
    while(true)
    {
        std::string input;
        std::getline(std::cin,input);
        if(input.empty())
            break;
        Point2D a;
        Point2Ddouble A;
        NSAanswer nearestSegment;
        int segments;
        std::vector<Point2D> Pval;
        INPUT(a,Pval,segments,input);
        if(!segments)
            return 0;
        nearestSegment = nearestSegmentAltitude(a,Pval);
        if(nearestSegment.Class)
        {
            A = calcPoint(a,Pval,nearestSegment);
        }
        else
        {
            A.x = Pval[nearestSegment.seg].x;
            A.y = Pval[nearestSegment.seg].y;
        }
        std::cout<< std::setprecision(2) << std::fixed << A.x << "\n" << A.y << "\n";
        input.clear();
    }
}
