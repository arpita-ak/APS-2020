#include<stdio.h>

int binary_search(int arr[],int l,int r,int x)
{
    int m;
    while(l<=r)
    {
        m=(l+r)/2;

        if(arr[m]==x)
            return m;
        else if(arr[m]<x)
            l=m+1;
        else
            r=m-1;
    }
    return -1;
}

int main()
{
    int arr[]={2,3,4,10,40};
    int n=5;
    int x;
    int res;
    printf("Binary  search: ");
    printf("\nEnter the element to be searched: ");
    scanf("%d",&x);
    res=binary_search(arr,0,n-1,x);
    if(res==-1)
        printf("\nElement not present in the given array");
    else
        printf("\%d is present at the index %d in the array",x,res);
    return 0;
}
