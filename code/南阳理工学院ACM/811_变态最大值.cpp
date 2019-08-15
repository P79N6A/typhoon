#include<stdio.h>
#include<iostream>
using namespace std;

int ThreeToMax(int a,int b ,int c);
int ThreeToMin(int a,int b ,int c);

int main()
{
	int n,i,sum,max;
	int *arr;
	while(scanf("%d",&n)!=EOF)
	{
		arr = new int[n];
		for(i=0;i<n;i++)
		{
			scanf("%d",&arr[i]);
		}
		for(i=0;i<n/3;i++)
		{
			if((i+1)%2==0)
				sum = ThreeToMin(arr[i*3] ,arr[i*3+1] ,arr[i*3+2]);
			else
				sum = ThreeToMax(arr[i*3] ,arr[i*3+1] ,arr[i*3+2]);
			if(i==0)
				max = sum;
			else
				if(max<sum) max = sum;
		}
		printf("%d\n",max);
	}
	return 0;
}

int ThreeToMax(int a,int b ,int c)
{
	int max;
	if(a>b) max=a;
	else max=b;
	if(max<c) max=c;
	return max;
}

int ThreeToMin(int a,int b ,int c)
{
	int min;
	if(a<b) min=a;
	else min=b;
	if(min>c) min=c;
	return min;
}