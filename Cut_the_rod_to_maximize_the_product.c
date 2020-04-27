//Program to cut the rod into many parts to maximize the product.

#include<stdio.h>
#include<stdlib.h>

int maximum_element(int a,int b,int c)
{
    if(a>b&&a>c)
        return a;
    else if(b>c)
        return b;
    else
        return c;
}
int main()
{
    int n,i,*rc,j,max;
    printf("Cut the rod into many parts such that the product is maximum: ");
    printf("\nEnter the length of the rod: ");
    scanf("%d",&n);
    rc=(int *)malloc(sizeof(int)*(n+1));
    for(i=0;i<n+1;i++)
        rc[i]=0;
    for(i=2;i<n+1;i++)
    {
        for(j=1;j<=i/2;j++)
        {
            max=maximum_element(rc[i],j*(i-j),j*rc[i-j]);
            rc[i]=max;
        }
    }
    printf("\nFor reference: ");
    for(i=0;i<n+1;i++)
        printf("%d ",rc[i]);
    printf("\nThe maximum product of the part of the rod of length %d is: %d",n,rc[n]);
    return 0;
}
