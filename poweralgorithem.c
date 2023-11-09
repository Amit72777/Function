// A raise to power b using recursion and algorithim
#include <stdio.h>
int power(int x, int y) // fuction decleration
{
    int m = 1;
    if (y == 0)
        return 1;
    if (y == 1)
        return x;

    if (y % 2 != 0)
        m = x;

    int z = power(x, y / 2); // function calling itself

    m = z * z * m;
    return m;
}
int main()
{
    int a, b; // intillization variable

    printf("Enter the base  number a :");
    scanf("%d", &a);
    printf("Enter the  power is b:");
    scanf("%d", &b);

    int c = power(a, b); // calling function
    printf(" \n the base is %d and the power is %d= %d ", a, b, c);

    return 0;
}