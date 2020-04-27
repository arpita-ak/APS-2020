//Program to find the number of set bits of a given number

#include<stdio.h>

int main()
{
    int n,a,result=0;
    printf("Number of set bits: ");
    printf("\nEnter the number whose number of set bits are to be computed: ");
    scanf("%d",&a);
    n=a;
    result=0;
    while(n)
    {
        result=result+1;
        n=n&n-1;
    }
    printf("\nThe number of set bits of the number %d is: %d",a,result);
    return 0;
}
