#include <stdio.h>

int power(int m, int n)
{
    int p = 1;
    for (int i = 1; i <= n; ++i)
    {
        p *= m;
    }
    return p;
}


int main()
{
    for (int i = 1; i < 10; ++i)
    {
        printf("%d %d\n", i, power(2, i));
    }
    return 0;
}
