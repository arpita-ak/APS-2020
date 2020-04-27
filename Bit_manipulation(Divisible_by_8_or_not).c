//Program to check if a number is divisible by 8 or not

#include<stdio.h>

int main()
{
    int n,result;
    printf("Divisible by 8 or not");
    printf("\nEnter the number to check for divisibility with 8: ");
    scanf("%d",&n);
    result=n;
    result=(result>>3)<<3;
    if(result==n)
        printf("\n%d is divisible by 8",n);
    else
        printf("\n%d is not divisible by 8",n);
    return 0;
}
