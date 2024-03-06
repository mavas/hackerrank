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
    int f_x, f_y;
    int u, v;
    unsigned int lcm, gcd;
    unsigned int answer;
    unsigned int report;

    f_x = fib(x);
    f_y = fib(y);
    u = pow(a, f_x) - 1;
    v = pow(a, f_y) - 1;
    printf("\tu = pow(a, f_x) - 1 = pow(%d, %d) - 1 = %d\n", a, f_x, u);
    printf("\tv = pow(a, f_y) - 1 = pow(%d, %d) - 1 = %d\n", a, f_y, v);
    lcm = std::lcm(u, v);
    printf("\tlcm = lcm(u, v) = lcm(%d, %d) = %d\n", u, v, lcm);
    gcd = std::gcd(u, v);
    printf("\tgcd = gcd(u, v) = gcd(%d, %d) = %d\n", u, v, gcd);
    answer = lcm / gcd;
    report = answer % m;

    printf("\t\tanswer = %d\n", answer);
    printf("\t\treport = %d\n", report);
}

void test()
{
    int valueFromLimits = INT_MAX;

    std::cout << "Value from climits "
         << "constant (maximum): ";
    std::cout << valueFromLimits << "\n";

    valueFromLimits = INT_MIN;
    std::cout << "Value from climits "
         << "constant(minimum): ";
    std::cout << valueFromLimits << "\n";

    // Using the wrap around property
    // of data types

    // Initialize two variables with
    // value -1 as previous and another
    // with 0 as present
    int previous = -1;
    int present = 0;

    // Keep on increasing both values
    // until the present increases to
    // the max limit and wraps around
    // to the negative value i.e., present
    // becomes less than previous value
    while (present > previous) {
        previous++;
        present++;
    }

    std::cout << "\nValue using the wrap "
         << "around property:\n";

    std::cout << "Maximum: " << previous << "\n";
    std::cout << "Minimum: " << present << "\n";
}


int main(int argc, char* argv[])
{
    int N;
    scanf("%d\n", &N);
    printf("%d test cases\n", N);
    //test();
    std::cout << sizeof(int) << "\n";
    std::cout << sizeof(unsigned int) << "\n";
    std::cout << sizeof(long) << "\n";
    std::cout << sizeof(long long) << "\n";
    std::cout << sizeof(unsigned long long) << "\n";

    unsigned long long x, y, a, m;
    for (int count = 0; count < N; count += 1)
    {
        if (count != 2) {
            scanf("%llu %llu %llu %llu\n", &x, &y, &a, &m);
            continue;
        }

        scanf("%llu %llu %llu %llu\n", &x, &y, &a, &m);
        printf("x = %llu, y = %llu, a = %llu, m = %llu\n", x, y, a, m);
        compute_the_answer(x, y, a, m);

        //std::string line2;
        //std::getline(std::cin, line2);
        //std::cout << "\t" << line2 << "\n";

        //char line[500];
        //scanf("%s\n", &line);
        //printf("\t%s\n", line);
    }

    return 0;
}
