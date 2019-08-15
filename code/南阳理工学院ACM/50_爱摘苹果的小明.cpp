#include<stdio.h>
int main()
{
	int arr[10],num;
	int n,i,high;
	scanf("%d",&n);
	while(n--)
	{
		high = 0;
		num = 0;
		for(i=0;i<10;i++)
			scanf("%d",&arr[i]);
		scanf("%d",&high);
		for(i=0;i<10;i++)
			if(high+30 >= arr[i])
				num++;
		printf("%d\n",num);
	}
	return 0;
}