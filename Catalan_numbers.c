//Program to find the Catalan numbers.

#include<stdio.h>
#include<stdlib.h>

int main()
{
    int i,j,n,*res,sum;
    printf("Catalan numbers: ");
    printf("\nEnter the Catalan number index: ");
    scanf("%d",&n);
    res=(int *)malloc(sizeof(int)*(n+1));
    res[0]=1;
    sum=1;
    for(i=0;i<n;i++)
    {
        sum=0;
        for(j=0;j<=i;j++)
        {
            sum=sum+res[j]*res[i-j];
        }
        res[i+1]=sum;
    }
    printf("\nThe Catalan number %d is: %d",n,sum);
    return 0;
}
