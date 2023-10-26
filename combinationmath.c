#include<stdio.h>
int fact( int n)
{
    int factorial=1;
    for(int i=1;i<=n;i++)
    {
        factorial=factorial*i;
    }
    return factorial;
}
int main()
{
    int  n,r,p;
    printf("Enter the number n:");
    scanf("%d",&n);
    printf("Enter the number r:");
    scanf("%d",&r);
    

    p = fact(n)/(fact(r)*fact(n-r));

    printf(" The combination is nCr= %d",p);

    return 0;
}