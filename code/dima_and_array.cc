/**
 * https://codeforces.com/gym/102069/problem/D
 */


#include <stdio.h>
#include <vector>
#include <algorithm>
#include <set>


int compute_mex(const std::set<int> new_set)
{
    int mex = -1;
    const int minimum = *new_set.begin();
    const int maximum = *new_set.rbegin();

    if (minimum > 0)
    {
        mex = 0;
        //printf("%d\n", mex);
    } else {
        int value = minimum + 1;
        for (; value <= maximum; value += 1)
        {
            //if (new_set.contains(value))
            //if (new_set.find(value) != new_set.end())
            if (new_set.count(value) == 0)
            {
                mex = value;
                //printf("\t\t\tMEX1: %d\n", mex);
                value = -1;
                break;
            }
        }
        if (value == (maximum + 1))
        {
            mex = value;
            //printf("\t\t\tMEX2: %d\n", mex);
        }
    }

    return mex;
}

void add_elements_to_set(std::set<int>& new_set, const int a[], const int left, const int right)
{
    for (int array_index = left - 1; array_index <= right - 1; array_index += 1)
    {
        new_set.insert(a[array_index]);
    }
}


int main(int argc, char* argv[])
{
    int N, Q;

    // Read the first line, which should be integers N and Q, separated by a
    // space.
    scanf("%d %d\n", &N, &Q);
    //printf("%d, %d\n", N, Q);

    // Read the next line, which should be an array of integers, and the array
    // is of length N
    int a[N];
    std::vector<int> a2;

    for (int i = 0; i < (N-1); i++)
    {
        scanf("%d ", &a[i]);
        a2.push_back(a[i]);
    }
    scanf("%d\n", &a[N-1]);
    a2.push_back(a[N-1]);

    //for (size_t i = 0; i < N; i++)
    //    printf("%d ", a[i]);
    //printf("\n");

    // Read and process each instruction line:
    int instruction = 0;
    while (instruction < Q)
    {
        // Each line looks like it contains exactly 3 items, each separated by
        // a space, with the first being a character, and the next two being an
        // integer
        char i;
        int left, right;

        // Read the three items, from the input, which should be the next
        // instruction to perform
        scanf("%c %d %d\n", &i, &left, &right);
        //printf("\tInstruction: %c %d %d\n", i, left, right);

        // Take an action based on the character..
        if (i == '?')
        {
            int mex = 2;
            //int new_a[right-left] = a[;

            //std::set<int> new_set_old(a2.begin()+left-1, a2.begin()+right-1);
            std::set<int> new_set;
            add_elements_to_set(new_set, a, left, right);
            //printf("\t\tMin/Max: %d %d\n", minimum, maximum);

            //std::multiset<int> multi(a+left-1, a+right-1);
            //std::multiset<int>::iterator itlow;
            //itlow = multi.lower_bound(0);
            //printf("\t\tMin: %d\n", *itlow);

            mex = compute_mex(new_set);

            ////std::set<int> new_a(a, 
            ////std::vector<int>
            //int counter = 0;
            //for (int value = minimum; value < maximum; value += 1)
            //{
          
            //    //if (new_set.count(value) == 0)
            //    //{
            //    //    printf("%d\n", value);
            //    //    //break;
            //    //}
            //}
            //for (int lower = left; lower < right; lower += 1)
            //{
            //    
            //}
            ////mex = *min_element(a2.begin()+left, a2.end()-right);
 
            printf("%d\n", mex);
        }
        else if (i == '!')
        {
            const int replacement_index = left - 1;
            const int replacement_value = right;

            a[replacement_index] = replacement_value;
            a2.at(replacement_index) = replacement_value;

            //printf("\t\tNew array: ");
            //for (size_t i = 0; i < N; i++)
            //{
            //    if (i == (N - 1))
            //    {
            //        printf("%d\n", a[i]);
            //        //printf("%d\n", a2.at(i));
            //    }
            //    else
            //    {
            //        printf("%d ", a[i]);
            //        //printf("%d ", a2.at(i));
            //    }
            //}
        }

        // Move to the next instruction..
        instruction += 1;
    }

    // ..
    return 0;
}
