#include<cstdio>
#include<cstring>
using namespace std;

int a[100+10],c[100+10];

int main()
{
	int m,n;
	memset(a,0,sizeof(a));
	memset(c,0,sizeof(c));
	int k=0;
	while(scanf("%d%d",&m,&n)==2&&m&&n)
	{
		a[m]+=n;
		c[k++]=m;
	}
	for(int i=0;i<110;i++)
	{
		if(a[c[i]]!=0)
		{
			printf("%d %d\n",c[i],a[c[i]]);
			a[c[i]]=0;
		}
	}
	return 0;
}