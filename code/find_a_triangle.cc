/**
 * https://codeforces.com/gym/102133/
 */


#include <stdio.h>


int main(int argc, char* argv[])
{
    int count = 0;

    int x1, y1, x2, y2;

    while (count < 600)
    {
        char c;

        printf("Q %d, %d, %d, %d\n", x1, y1, x2, y2);
        scanf("%c", &c);

        count += 1;
    }

    return 0;
}
