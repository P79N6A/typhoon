#include<stdio.h>
int change(int x)
{
	int s=0;
	while(x)
	{
		s=s*10+x%10;
		x/=10;
	}
	return s;
}
int zhi(int a,int b,int c[])
{
	int i;
	for(i=0;i<(b-a+1);i++)
	c[i]=a+i;
}
int main()
{
	int a,b,N;
	scanf("%d",&N);
	while(N--)
	{
		int t,i,j,m,c[50];
		scanf("%d%*c%d",&a,&b);
		zhi(a,b,c);
		for(i=0;i<(b-a);i++)
		{
			m=i;
			for(j=i;j<(b-a+1);j++)
				if(change(c[j])<change(c[m]))m=j;
			if(m!=i)
			{
				t=c[i];
				c[i]=c[m];
				c[m]=t;
			}
		}
		for(i=0;i<(b-a+1);i++)
			printf("%d ",c[i]);
		printf("\n");
	}
}