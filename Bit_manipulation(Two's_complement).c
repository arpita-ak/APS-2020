//Program to find the two's complement of a given number.

//can be done using either
//1) -n
//2) ~n+1

#include<stdio.h>

int main()
{
    int n,res1,res2;
    printf("Two complement of a number: ");
    printf("\nEnter a number whose two's complement is to be found: ");
    scanf("%d",&n);
    res1=-n;
    res2=~n+1;
    printf("\nThe two's complement of %d using -%d is :%d",n,n,res1);
    printf("\nThe two's complement of %d using ~%d+1 is: %d",n,n,res2);
    return(0);
}
