#include <stdio.h>
#include <math.h>
int main()
{
    int a = 10, b = 20;

    swap(a, b);
    printf("\n a=%d \t b=%d ", a, b);
    return 0;
}
int swap(m, n)
int m;
int n;
{
    int t;
    t = m;
    m = n;
    n = t;
    printf(" m=%d n=%d ", m, n);
    return m, n;
}