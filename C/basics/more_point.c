#include <stdio.h>

void Print_Num(int *number)
{
    printf("The integer stored is %d, this is at memory address %p\n", *number, number);
}

int main()
{
    int age = 21;
    int *pAge = &age;

    printf("age ADDRESS: %p\n", &age);
    //printf("pAge VALUE: %p\n", pAge);
    //
    //printf("age VALUE: %d\n", age);
    //printf("VALUE stored at pAge: %d\n", *pAge);
    
    Print_Num(pAge);
    return 0;
}
