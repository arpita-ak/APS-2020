//Program to find the maximum sum of the sub-array in the given array
#include<stdio.h>
#include<stdlib.h>

int main()
{
    int *a,i,n,tmax=0,max=0,max_all;
    printf("Kadane algorithm");
    printf("\nEnter the number of array elements: ");
    scanf("%d",&n);
    a=(int *)malloc(sizeof(int)*n);
    for(i=0;i<n;i++)
    {
        scanf("%d",&a[i]);
    }
    for(i=0;i<n;i++)
    {
        tmax=tmax+a[i];
        if(tmax<0)
            tmax=0;
        if(max<tmax)
            max=tmax;
    }
    printf("\nThe maximum sum of the sub array is: %d",max);
    return 0;
}
