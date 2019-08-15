#include<stdio.h>
int main()
{
	int n,k,i,m;
	while(1)
	{
		m=0;
		scanf("%d%d",&n,&k);
		if(n==0&&k==0) 
			break;
		for(i=1;i<=n/2;i++)
			if(i*(n-i)==k) m=1;
		if(m==0) 
			printf("NO\n");
		else 
			printf("YES\n");
	}
	return 0;
}