#include<stdio.h>
int main()  
{  
    int a,b,i,t;  
    while(scanf("%d%d",&a,&b)!=EOF)  
    {  
        long long m=0,c=0;  
        for(t=1;t<=b;t++)  
        {  
            m+=t;  
        }  
        for(i=1;i<=a;i++)  
        {  
            c+=m*i;  
        }  
        printf("%lld\n",c);  
    }  
    return 0;  
}  