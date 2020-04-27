//Program to find the particular binomial coefficients using recursive functions

#include<stdio.h>

int bn_coeff(int n,int k)
{
    if(k==0||k==n)
        return 1;
    else
        return bn_coeff(n-1,k-1)+bn_coeff(n-1,k);
}

int main()
{
    int n,k,res;
    printf("Binomial coefficients: ");
    printf("\nEnter the value of n: ");
    scanf("%d",&n);
    printf("Enter the value of k: ");
    scanf("%d",&k);
    if(n>=k)
    {
      res=bn_coeff(n,k);
      printf("\nThe value of binomial coefficients for n= %d and k= %d is: %d",n,k,res);
    }
    else
        printf("\nThe binomial coefficients is not possible for n=%d and k=%d",n,k);
    return 0;
}
