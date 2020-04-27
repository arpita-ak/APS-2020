//Program to find the nth Carol number.

#include<stdio.h>
#include<math.h>

int carol_number(int n)
{
    int result;
    result=pow(2,n)-1;
    return (result*result-2);
}

int main()
{
    int num;
    printf("Carol number");
    printf("\nEnter the Carol number to be found: ");
    scanf("%d",&num);
    printf("\nThe %d Carol number is: %d",num,carol_number(num));
}
