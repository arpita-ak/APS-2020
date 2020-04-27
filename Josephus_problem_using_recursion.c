//Program for Josephus problem using recursion.
#include<stdio.h>

int josephus(int n)
{
    if(n==1)
        return 1;
    else if(n%2==0)
        return (2*josephus(n/2)-1);
    else
        return (2*josephus(n/2)+1);
}

int main()
{
    int n;
    printf("Josephus problem using bit manipulation.");
    printf("\nEnter the number of people: ");
    scanf("%d",&n);
    printf("\nThe person who survives is: %d",josephus(n));
    return 0;
}

