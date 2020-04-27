//Program to find the binomial coefficients using single 1D array.

#include<stdio.h>
#include<string.h>

int bn_coeff(int n,int k)
{
    int c[k+1],min,i,j;
    memset(c,0,sizeof(c));
    c[0]=1;
    printf("\n");
    for(i=1;i<=n;i++)
    {
        if(i>k)
            min=k;
        else
            min=i;
        for(j=min;j>0;j--)
            c[j]=c[j]+c[j-1];
    }
    printf("\nThe array is: ");
    for(i=0;i<=k;i++)
    {
        printf("%d ",c[i]);
    }
    return c[k];
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
       printf("\nThe value of the binomial coefficients for n=%d and k=%d is: %d",n,k,res);
    }
    else
        printf("\nThe value of the binomial coefficient cannot be found for n=%d and k=%d",n,k);
    return 0;
}
