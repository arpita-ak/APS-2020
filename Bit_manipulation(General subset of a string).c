//Program to find all possible subsequences of a string using bit manipulation.
//Print first nothing and then prints the subsequence for i>0.
#include<stdio.h>
#include<math.h>
#include<string.h>

int main()
{
    char data[100];
    int set_size;
    unsigned int size;
    int i,j;
    printf("Enter the string whose sub-sequence are to be found: ");
    scanf("%s",data);
    set_size=strlen(data);
    size=pow(2,set_size);
    printf("\nThe sub-sequence of the string %s are: ",data);
    for(i=0;i<size;i++)
    {
        for(j=0;j<set_size;j++)
        {
            if(i&(1<<j))
                printf("%c",data[j]);
        }
        printf("\n");
    }
    return 0;
}

