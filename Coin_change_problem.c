//Coin change problem.

#include<stdio.h>
#include<stdlib.h>

int coinChange(int coin[],int x,int N)
{
    int i,j;
    int dp[N+1][x];
    int including,excluding;
    for(j=0;j<x;j++)
        dp[0][j]=1;

    for(i=1;i<=N;i++)
    {
        for(j=0;j<x;j++)
        {
            if(i>=coin[j])
                including=dp[i-coin[j]][j];
            else
                including=0;

            if(j>=1)
                excluding=dp[i][j-1];
            else
                excluding=0;

            dp[i][j]=including+excluding;
        }
    }
    return dp[N][x-1];
}

int main()
{
    int i,x,N;
    printf("Coin change problem using dynamic programming");
    printf("\nEnter the amount whose change is required: ");
    scanf("%d",&N);

    printf("\nEnter the number of distinct values of coins: ");
    scanf("%d",&x);

    int coin[x];
    printf("\nEnter the values of coins: ");
    for(i=0;i<x;i++)
        scanf("%d",&coin[i]);
    printf("\nThe number of ways is: %d",coinChange(coin,x,N));
    return 0;
}
