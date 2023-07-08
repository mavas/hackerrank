/**
 * https://codeforces.com/gym/102069/problem/D
 */


#include <stdio.h>
#include <vector>
#include <algorithm>
#include <set>


int main(int argc, char* argv[])
{
    int N, Q;

    // Read the first line, which should be integers N and Q, separated by a
    // space.
    scanf("%d %d\n", &N, &Q);
    printf("%d, %d\n", N, Q);

    // Read the next line, which should be an array of integers (of length N)
    int a[N];
    std::vector<int> a2;

    for (int i = 0; i < (N-1); i++)
    {
        scanf("%d ", &a[i]);
        a2.push_back(a[i]);
    }
    scanf("%d\n", &a[N-1]);

    for (size_t i = 0; i < N; i++)
        printf("%d ", a[i]);
    printf("\n");

    // Read and process each instruction line:
    int instruction = 0;
    while (instruction < N)
    {
        // Each line looks like it contains exactly 3 items, each separated by
        // a space, with the first being a character, and the next two being an
        // integer
        char i;
        int left, right;

        // Read the three items
        scanf("%c %d %d\n", &i, &left, &right);
        printf("\t%c %d %d\n", i, left, right);

        // Take an action based on the character..
        if (i == '?')
        {
            int mex = 2;
            //std::set<int> new_a(a, 
            //std::vector<int>
            int so_far = 0;
            for (int lower = left; lower < right; lower += 1)
            {
                
            }
            //mex = *min_element(a2.begin()+left, a2.end()-right);
            printf("%d\n", mex);
        }
        else if (i == '!')
        {
            a[left-1] = right;
        }

        // Move to the next instruction..
        instruction += 1;
    }

    // ..
    return 0;
}
