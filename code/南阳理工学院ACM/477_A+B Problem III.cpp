#include<stdio.h>
int main()
{
	int t;
	scanf("%d",&t);
	while(t--)
	{
		double m,n,k;
		scanf("%lf %lf %lf",&m,&n,&k);
		if(m+n-k<=0.0001 && m+n-k>=-0.0001)//她就是那个坑
		printf("Yes\n");
		else 
		printf("No\n");
	}
	return 0;
}