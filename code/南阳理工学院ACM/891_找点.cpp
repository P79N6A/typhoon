//贪心算法——区间问题
//思路:先按右端点由小到大排序，相等的话左端点由大到小
#include<algorithm>
#include<stdio.h>
using namespace std;
bool compare(int* a,int* b)
{
	if(a[1]!=b[1])
		return a[1]<b[1];
	else
		return a[0]>b[0];
}
int main()
{
	int i,N,num,right;
	int **arr;
	while(scanf("%d",&N) != EOF)
	{
		num = 0;
		right = -1;
		arr = new int*[N];
		for(i=0;i<N;i++)
		{
			arr[i] = new int[2];
			scanf("%d %d",&arr[i][0],&arr[i][1]);
		}
		sort(arr,arr + N,compare);
		for(i=0;i<N;i++)
			if(arr[i][0]>right)
			{
				right = arr[i][1];
				num++;
			}
		printf("%d\n",num);
	}
	return 0;
}