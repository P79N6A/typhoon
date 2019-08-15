#include<stdio.h>
int arr[10000];
int main()
{
	int n,i,num,sum,j;
	while(scanf("%d",&n)!=EOF)
	{
		for(i=0;i<n;i++)
		scanf("%d",&arr[i]);
		sum = 0;
		num = 0;
		for(i=0;i<n-num;i++)    
		if(arr[i]==1)
		{
			if(i!=0 && (i==n-num-1 || arr[i+1]>arr[i-1] || arr[i-1]==2))
				arr[i-1]++;
			else if(i!=n-num && (i==0 || arr[i+1]<=arr[i-1]))
				arr[i+1]++;
			for(j=i+1;j<n-num;j++)
				arr[j-1] = arr[j];
			num++;
		}
		for(i=1,sum=arr[0];i<n-num;i++)
		{
			sum *= arr[i];
			if(sum > 10086)
			sum = sum % 10086;
		}
		printf("%d\n",sum);
	}
	return 0;
}