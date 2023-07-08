/**
 * https://codeforces.com/gym/104022/problem/I
 */


#include <stdio.h>
#include <iostream>
#include <cmath>
#include <numeric>
#include <climits>


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
    int f_x;
    int f_y;
    int u;
    int v;
    int lcm;
    int gcd;
    uint answer;
    uint report;

    f_x = fib(x);
    f_y = fib(y);
    u = pow(a, f_x) - 1;
    v = pow(a, f_y) - 1;
    lcm = std::lcm(u, v);
    gcd = std::gcd(u, v);
    answer = lcm / gcd;
    report = answer % m;

    printf("\t\tanswer = %d\n", answer);
    printf("\t\treport = %d\n", report);
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
        printf("\tx = %d, y = %d, a = %d, m = %d\n", x, y, a, m);
        compute_the_answer(x, y, a, m);

        //std::string line2;
        //std::getline(std::cin, line2);
        //std::cout << "\t" << line2 << "\n";

        //scanf("%s\n", &line);
        //printf("\t%s\n", line);
    }

    return 0;
}
