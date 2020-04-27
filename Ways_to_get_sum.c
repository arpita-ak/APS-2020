//Ways to get a given sum using the numbers.
#include<stdio.h>
#include<string.h>

int main()
{
    int *a,*digits,max_sum,i,j,k,n;
    printf("Enter the maximum sum to be obtained: ");
    scanf("%d",&max_sum);
    printf("\nEnter the number of numbers to be used to obtain the sum of %d: ",max_sum);
    scanf("%d",&n);
    digits=(int *)malloc(sizeof(int)*n);
    printf("\nEnter the %d numbers: \n",n);
    for(i=0;i<n;i++)
        scanf("%d",&digits[i]);
    a=(int *)malloc(sizeof(int)*(max_sum+1));
    memset(a,0,(max_sum+1)*(sizeof(a[0])));
    a[0]=1;
    for(i=0;i<n;i++)
    {
        for(k=0,j=digits[i];j<max_sum+1;k++,j++)
        {
            if(a[k]==1)
                a[j]=a[j]+1;
        }
    }
    printf("\nThe number of ways to obtain the sum from 0 to %d is: ",max_sum);
    for(i=0;i<max_sum+1;i++)
        printf("\n%d->%d",i,a[i]);
    printf("\nThe number of ways to obtain the sum of %d is: %d",max_sum,a[max_sum]);
    return 0;
}
