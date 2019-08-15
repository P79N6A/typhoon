#include<stdio.h>
#include<algorithm>
using namespace std;
bool compare(int *a,int *b)
{
	if(a[0]==b[0])
		return a[1]<b[1];
	return a[0]<b[0];
}
int main()
{
	int T,N,time,l,w,i,j,num;
	int **arr;
	scanf("%d",&T);
	while(T--)
	{
		time = 0; 
		num = 0;
		scanf("%d",&N);
		arr = new int*[N];
		for(i=0;i<N;i++)
		{
			arr[i] = new int[3];
			scanf("%d %d",&arr[i][0],&arr[i][1]);
			arr[i][2] = 0;
		}
		sort(arr,arr+N,compare);
		while(num!=N)
		{
			l=0;
			w=0;
			for(i=0;i<N;i++)
			{
				if(arr[i][2]==0 && l<=arr[i][0] && w<=arr[i][1])
				{
					l = arr[i][0];
					w = arr[i][1];
					arr[i][2] = 1;
					num++;
				}
			}
			time++;
		}
		printf("%d\n",time);
	}
	return 0;
}