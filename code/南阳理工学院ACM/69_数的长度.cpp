#include <stdio.h>
#include <math.h>
int main()
{
	int n,cas,i;
	double sum;
	scanf("%d",&cas);
	while (cas--)
	{
		scanf("%d",&n);
		sum=1;
		for(i=1;i<=n;i++)
			sum+=log10((double)i);
		printf("%d\n",(int)sum);
	}
	return 0;
}