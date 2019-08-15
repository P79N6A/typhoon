#include<stdio.h>
#include<iostream>
#include<algorithm>
using namespace std;

bool compare(int a[2],int b[2])
{
	if(a[0]*a[1] == b[0]*b[1])
		return a[1] < b[1];
	return a[0]*a[1] < b[0]*b[1];
}
int main()
{
	int n,i,j,max=0,sum;
	int **arr;
	scanf("%d",&n);
	arr = new int*[n+1];
	for(i=0;i<=n;i++)
	{
		arr[i] = new int[2];
		scanf("%d %d",&arr[i][0],&arr[i][1]);
	}
	sort(arr+1,arr+n+1,compare);
	sum = arr[0][0];
	for(i=1;i<=n;i++)
	{
		if(max < sum/arr[i][1])
			max = sum/arr[i][1];
		sum*=arr[i][0];
	}
	printf("%d\n",max);
	return 0;
}