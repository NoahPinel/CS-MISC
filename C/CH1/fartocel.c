#include <stdio.h>

/*
 * Just macro, when compiled the 'macro' will be dropped in place
 * e.g.,
 * int a = BOUND --> integer a == 300
 * char b = step --> char b == '20' */

#define BOUND 300
#define STEP 20

/* Print far to cel for some range */
int main()
{
    float far = 0;
    float cel = 0;

    while (far <= BOUND)
    {
        cel = (far - 32) * (5.0 / 9.0);
        printf("F:%3.f\tC:%6.2f\n", far, cel);
        far += STEP;
    }
    
    return 0;
}
