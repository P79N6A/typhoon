#include<stdio.h>

int main()
{
	int n,i,id,sum;
	int arr[7][2];
	scanf("%d",&n);
	while(n--)
	{
		id = 0;
		sum = 0;
		for(i=0;i<7;i++)
			scanf("%d %d",&arr[i][0],&arr[i][1]);
		for(i=0;i<7;i++)
			if(arr[i][0]+arr[i][1] > 8 && arr[i][0]+arr[i][1]>sum)
			{
				id = i+1;
				sum = arr[i][0]+arr[i][1];
			}
		printf("%d\n",id);
	}
	return 0;
}