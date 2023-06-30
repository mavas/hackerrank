/**
 * https://codeforces.com/gym/104022/problem/I
 */


#include <stdio.h>
#include <iostream>


int fib(const int n)
{
    if (n == 1 || n == 2) {
        return 1;
    } else {
        return fib(n-1) + fib(n-2);
    }
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
        std::string line2;

        std::getline(std::cin, line2);
        std::cout << "\t" << line2 << "\n";

        //scanf("%s\n", &line);
        //printf("\t%s\n", line);
    }

    return 0;
}
