#include<stdio.h>
using namespace std;
int x,y,a[101][101];
void del(int z,int c)
{
	if(z>0 && a[z-1][c]==1)
	{
		a[z-1][c]=0;
		del(z-1,c);
	}
	if(z<x-1 && a[z+1][c]==1)
	{
		a[z+1][c]=0;
		del(z+1,c);
	}
	if(c>0 && a[z][c-1]==1)
	{
		a[z][c-1]=0;
		del(z,c-1);
	}
	if(c<y-1 && a[z][c+1]==1)
	{
		a[z][c+1]=0;
		del(z,c+1);
	}
}

int main()
{
	int n;
	scanf("%d",&n);
	while(n--)
	{
		int sum=0; 
		scanf("%d %d",&x,&y);
		for(int i=0;i<x;i++)
			for(int j=0;j<y;j++)
				scanf("%d",&a[i][j]);
		for(int i=0;i<x;i++)
			for(int j=0;j<y;j++)
				if(a[i][j]==1)
				{
					sum++;
					del(i,j);
				}
		printf("%d\n",sum);
	}
	return 0;
}