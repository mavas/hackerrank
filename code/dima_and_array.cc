/**
 * https://codeforces.com/gym/102069/problem/D
 */


#include <stdio.h>


int main(int argc, char* argv[])
{
    int N, Q;
    scanf("%d %d\n", &N, &Q);
    printf("%d, %d\n", N, Q);

    int a[N];

    for (int i = 0; i < (N-1); i++)
    {
        scanf("%d ", &a[i]);
    }
    scanf("%d\n", &a[N-1]);
    for (size_t i = 0; i < N; i++)
        printf("%d ", a[i]);
    printf("\n");

    return 0;
}
