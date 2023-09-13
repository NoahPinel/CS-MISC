#include <stdio.h>

int main()
{
    int x = 1;
    int y = 2;
    int z[10];
    int *ip;

    ip = &x; /* ip --> x */
    printf("%d", *ip);
    
    y = *ip; /* y == 1 b/c ip --> x, x == 1 */
    printf("%d", y);
    
    *ip = 0; /* x == 0 b/c *ip eq x */
    printf("%d", *ip);
    printf("%d", x);
   
    ip = &z[10]; /* ip --> z[0] */
    printf("%d", *ip);
    
    return 0;
}


