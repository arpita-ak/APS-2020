//Ways to get a sum of 15 using 3,5,10
#include<stdio.h>
#include<string.h>

int main()
{
    int digits[]={3,5,10},max_sum,i,j,k,a[100];
    printf("\nEnter the sum to be obtained using 3,5,10: ");
    scanf("%d",&max_sum);
    memset(a,0,(max_sum+1)*sizeof(a[0]));
    a[0]=1;
    for(i=0;i<3;i++)
    {
        for(k=0,j=digits[i];j<max_sum+1;k++,j++)
        {
            if(a[k]==1)
                a[j]=a[j]+1;
        }
    }
    printf("\nThe number of ways to obtain the sum of %d is: %d",max_sum,a[max_sum]);
    return 0;
}
