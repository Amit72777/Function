// using function check weather the number are strong number or not 

#include <stdio.h>
int fact(int n)
{
    int fact = 1;
    for (int i = 1; i <= n; i++)
    {
        fact = fact * i;
    }
    return fact;
}

int main()
{
    int t, n, strong = 0, a;
    printf("\n Check weather the  input number is strong number or not \n\n");
    printf("Enter the number :");
    scanf("%d", &n);
    a = n;
    do
    {
        t = n % 10;
        strong = strong + fact(t);
        n /= 10;

    } while (n > 0);

    if (strong == a)
    {
        printf(" \n %d is a strong number ", strong);
    }
    else
        printf("%d is not a strong number ", a);
    return 0;
}