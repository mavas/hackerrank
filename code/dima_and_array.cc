/**
 * https://codeforces.com/gym/102069/problem/D
 *
 * Possible strategy: You can seek the input, and look ahead and find all '!'
 * operations, and see where they overlap with the ranges specified by 'left'
 * and 'right', and see if that can help you out somehow in making a more
 * optimal solution.
 *
 * int min = *min_element(v1.begin(), v1.end());
 */


#include <stdio.h>
#include <vector>
#include <algorithm>
#include <iostream>
#include <set>
#include <sys/types.h>
#include <unistd.h>


void print_array_2(const int a[], const int N)
{
    for (size_t i = 0; i < N; i++)
        printf("%d ", a[i]);
    printf("\n");
}


void print_array(const int a[], const int N)
{
    printf("\t\tNew array: ");
    for (size_t i = 0; i < N; i++)
    {
        if (i == (N - 1))
        {
            printf("%d\n", a[i]);
            //printf("%d\n", a2.at(i));
        }
        else
        {
            printf("%d ", a[i]);
            //printf("%d ", a2.at(i));
        }
    }
}


int compute_mex_method_1(const int a[], const int left, const int right)
{
    std::multiset<int> multi(a+left-1, a+right-1);
    std::multiset<int>::iterator itlow;
    itlow = multi.lower_bound(0);
    printf("\t\tMin: %d\n", *itlow);
    return 0;
}


int compute_mex_method_2()
{
    ////s/td::set<int> new_a(a, 
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
    return 0;
}


int compute_mex(const std::set<int> sub_array_set)
{
    int mex = -1;
    const int minimum = *sub_array_set.begin();
    const int maximum = *sub_array_set.rbegin();

    if (minimum > 0)
    {
        mex = 0;
        //printf("%d\n", mex);
        return mex;
    } else {
        int value = minimum + 1;
        for (; value <= maximum; value += 1)
        {
            //if (new_set.contains(value))
            //if (new_set.find(value) != new_set.end())
            if (sub_array_set.count(value) == 0)
            {
                mex = value;
                //printf("\t\t\tMEX1: %d\n", mex);
                return mex;
                value = -1;
                break;
            }
        }
        if (value == (maximum + 1))
        {
            mex = value;
            //printf("\t\t\tMEX2: %d\n", mex);
            return mex;
        }
    }

    return mex;
}


void add_elements_to_set(std::set<int>& sub_array_set, const int a[], const int left, const int right)
{
    for (int array_index = left - 1; array_index <= right - 1; array_index += 1)
    {
        sub_array_set.insert(a[array_index]);
    }
}


/**
 * This makes extensive use of the std:: namespace (whereas solution_1 makes
 * more extensive use of C-style interface).
 */
void solution_2()
{
    int N, Q;

    std::scanf("%d %d\n", &N, &Q);
    //printf("%d, %d\n", N, Q);

    std::vector<int> a;
    int temp;
    for (int i = 0; i < (N-1); i++)
    {
        scanf("%d ", &temp);
        a.push_back(temp);
    }
    std::scanf("%d\n", &temp);
    a.push_back(temp);
}


void find_lines_of_modifications()
{
    // Get current seek position, so we can set it back after this function
    // call is over.
    //printf("seek: %s\n", std::tellg());
}


void read_array_from_stdin(int* a, const int N)
{
    for (int i = 0; i < (N-1); i++)
    {
        scanf("%d ", &a[i]);
    }
    scanf("%d\n", &a[N-1]);
}


/** This path involves use of C-style function calls. */
void solution_1()
{
    int N, Q;

    scanf("%d %d\n", &N, &Q);

    // Read the next line, which should be an array of integers, and the array
    // is of length N
    int a[N];
    read_array_from_stdin(a, N);
    //print_array_2(a, N);

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
            std::set<int> sub_array_set;
            add_elements_to_set(sub_array_set, a, left, right);
            //printf("\t\tMin/Max: %d %d\n", minimum, maximum);
            mex = compute_mex(sub_array_set);

            printf("%d\n", mex);
        }
        else if (i == '!')
        {
            const int replacement_index = left - 1;
            const int replacement_value = right;

            a[replacement_index] = replacement_value;
            //a2.at(replacement_index) = replacement_value;
            //print_array(a, N);
        }

        // Move to the next instruction..
        instruction += 1;
    }
}


int main(int argc, char* argv[])
{
    // Read the first line, which should be integers N and Q, separated by a
    // space.

    solution_1();
    //solution_2();

    return 0;
}


/**
 * #include <sys/types.h>
 * #include <unistd.h>
 */
void print_if_stdin_is_seekable()
{
    if(lseek(STDIN_FILENO,0, SEEK_CUR) == -1)
        printf("cannot seek\n");
    else{
        printf("seek ok\n");
    }
}
