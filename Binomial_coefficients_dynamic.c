//Program to find the binomial coefficients till the given number using dynamic programming.

#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main()
{
    int n,k,**a,i,j;
    printf("Binomial coefficients: ");
    printf("\nEnter the value of n: ");
    scanf("%d",&n);
    printf("Enter the value of k: ");
    scanf("%d",&k);
    a=(int **)malloc(sizeof(int *)*n);
    for(i=0;i<n;i++)
    {
        a[i]=(int *)malloc(sizeof(int)*k);
        memset(a[i],0,sizeof(int)*k);
    }
    for(i=0;i<n;i++)
    {
        for(j=0;j<=k&&j<=i;j++)
        {
            if(i==j||j==0)
               a[i][j]=1;
            else
                a[i][j]=a[i-1][j-1]+a[i-1][j];
        }
    }
    printf("\nThe binomial coefficients with n=%d and k=%d is: \n",n,k);
    for(i=0;i<n;i++)
    {
        for(j=0;j<n;j++)
            printf("%d ",a[i][j]);
        printf("\n");
    }
    return(0);
}
