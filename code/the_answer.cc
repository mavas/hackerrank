/**
 * https://codeforces.com/gym/104022/problem/I
 */


#include <stdio.h>
#include <iostream>
#include <cmath>


int fib(const int n)
{
    if (n == 1 || n == 2) {
        return 1;
    } else {
        return fib(n-1) + fib(n-2);
    }
}


void compute_the_answer(const int x, const int y, const int a, const int m)
{
    const int f_x = fib(x);
    const int f_y = fib(y);
    const int u = pow(a, f_x) - 1;
    const int v = pow(a, f_y) - 1;
}


int main(int argc, char* argv[])
{
    int N;
    scanf("%d\n", &N);
    printf("%d test cases\n", N);

    int test_cases[N];

    for (int count=0; count < N; count+=1)
    {
        char line[500];

        int x, y, a, m;
        scanf("%d %d %d %d\n", &x, &y, &a, &m);
        printf("x = %d, y = %d, a = %d, m = %d\n", x, y, a, m);
        compute_the_answer(x, y, a, m);

        //std::string line2;
        //std::getline(std::cin, line2);
        //std::cout << "\t" << line2 << "\n";

        //scanf("%s\n", &line);
        //printf("\t%s\n", line);
    }

    return 0;
}
