#include<stdio.h>
#include<string.h>
#include<iostream>
using namespace std;
string Del(string arr,int i,int num)
{
	int j;
	for(j=i;j<num-1;j++)
		arr[j] = arr[j+1];
	return arr;
}
int main()
{
	int T,i,j,sum,num;
	string arr;
	scanf("%d",&T);
	while(T--)
	{
		cin>>arr>>sum;
		num = arr.length();
		for(i=0;i<sum;i++)
			for(j=0;j<num-i;j++)
				//每次删除左比右小的数，如果没有删除最后一个
				if(j == num-i-1 || arr[j]<arr[j+1])
				{
					arr = Del(arr,j,num-i);
					break;
				}
		for(i=0;i<num-sum;i++)
			cout<<arr[i];
		cout<<endl;
	}
	return 0;
}        