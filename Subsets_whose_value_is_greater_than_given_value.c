//Returns the number of subsets whose sum is greater than or equal to the given value.

#include<stdio.h>
#include<math.h>

int subset_sum(int set[],int set_size,int value)
{
    int count=0;
    int x,sum=0,k;
    for(x=0;x<pow(2,set_size);x++)
    {
        //to generate every possible sub-sets.
        for(k=0;k<set_size;k++)
        {
            //to check the number generated sum is value or not.
            //check if kth bit is set in x or not.
            if((x&(1<<k)))
            {
                //if it is satisfied add the kth item from a set and add it to sum.
                sum=sum+set[k];
            }
        }
        if(sum>value)
        {
           //here sum is greater than value so increment the count.
           count++;
        }
    }
    return count;
}

int main()
{
    int set[]={3,5,2},set_size=3,value=4,res;
    printf("Returns the number of subsets whose sum is greater than or equal to the given value: ");
    res=subset_sum(set,set_size,value);
    printf("\nThe number of subsets whose value is greater than %d is: %d",value,res);
    return(0);
}
