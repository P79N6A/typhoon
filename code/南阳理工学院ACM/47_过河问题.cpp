//贪心算法 分两种情况：
//1.最快的把手电筒送回来，然后最慢的和次慢的一起过河，最后次快的把最快的接回来；
//2.最快的来回二趟
 
#include<stdio.h>
#include<algorithm>
#include<cmath>
using namespace std;
int main()
{
	int T,N,i,j,time,manNum;
	int *arr;
	scanf("%d",&T);
	while(T--)
	{
		time = 0;
		scanf("%d",&N);
		arr = new int[N];
		for(i=0;i<N;i++)
			scanf("%d",&arr[i]);
		sort(arr,arr+N);
		manNum = N;
		if(manNum>=2)
			time += arr[1];
		else
			time += arr[0];
		while(manNum>2)
			if(manNum > 3)
			{
				time += min(2 * arr[1] + arr[0] + arr[manNum-1] ,2 * arr[0] + arr[manNum-2] + arr[manNum-1]);
				manNum -= 2;
			}
			else
			{
				time += arr[0] + arr[manNum-1];
				manNum -= 3;
			}
		printf("%d\n",time);
	}
	return 0;
}