#include<iostream>
using namespace std;

int main()
{
    int T,i,j,N,Q,A,even=0,odd=0,count=0;
    
    scanf("%d",&T);
    for (j=0;j<T;j++)
    {
        scanf("%d",&N);
        scanf("%d",&Q);
        
        for (i=0;i<N;i++)
        {
            scanf("%d",&A);
            count=__builtin_popcount(A);
            if (count&1==1)
            {
                odd=odd+1;
                
            }
            else
            {
                even=even+1;
            }
            count=0;
        }
        
        for (i=0;i<Q;i++)
        {
            scanf("%d",&A);
            count=__builtin_popcount(A);
            if (count&1==1)
            {
                printf("%d %d\n",odd,even);
            }
            else
            {
                printf("%d %d\n",even,odd);
            }
            count=0;
        }
        even=0;
        odd=0;
        
    }
}