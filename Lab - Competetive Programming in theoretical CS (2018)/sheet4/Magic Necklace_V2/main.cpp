#include <iostream>
#include <string>
#include <sstream>
#include <vector>       // std::vector
#include <math.h>       /* ceil */

struct LongIncSubS
{
    int maxValue;
    int lisSize;
};

LongIncSubS LongestIncreasingSubsequence(std::vector<int> input)
{
    std::vector<int> sub_seq;
    LongIncSubS answer;
    sub_seq.resize(input.size(),0);

    int lenght_sub = 0;
    int low,high,mid,pos;
    for (int i = 0;i<input.size();i++)
    {
        low = 1;
        high = lenght_sub;

        while(low <= high)
        {
            mid = (low + high + 1) / 2;

            if(input[sub_seq[mid]] < input[i])
                low = mid + 1;
            else
                high = mid - 1;
        }

        pos = low;
        sub_seq[pos] = i;
        if (pos > lenght_sub)
            lenght_sub = pos;
    }
    answer.lisSize = lenght_sub;
}

int main()
{

}
