//Program to find the length of the longest consecutive zeros in the binary representation of a number.
#include<stdio.h>

int count_it(int n)
{
    int  maxm=-1;
    int count=0;
    while(n)
    {
        if(!(n&1))
        {
            count++;
            n>>=1;
            //maxm=max(maxm,count);
            if(maxm<count)
                maxm=count;
        }
        else
        {
            //maxm=max(maxm,count);
            if(maxm<count)
                maxm=count;
            count=0;
            n>>=1;
        }
    }
    return maxm;
}

int main()
{
    int num;
    printf("Length of longest consecutive zeros in the binary representation of a number.");
    printf("\nEnter the number: ");
    scanf("%d",&num);
    printf("\nLength of longest consecutive zeros in the binary representation of a number %d is: %d",num,count_it(num));
    return 0;
}
