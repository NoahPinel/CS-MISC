#include <stdio.h>

#define N 5

int main() 
{
  int a[N];

  printf("populate the array\n");
  for (int i = 0; i < N; i++) 
  {
    printf("index %d: ", i);
    scanf(" %d", & a[i]);
  }

  printf("array\n");
  for (int i = 0; i < N; i++) 
  {
    printf(" %d ", a[i]);
  }

  printf("\nreversed array\n");
  for (int i = N - 1; i >= 0; i--) 
  {
    printf(" %d ", a[i]);
  }
  printf("\n");

  return 0;
}
