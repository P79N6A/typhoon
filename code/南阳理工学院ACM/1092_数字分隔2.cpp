#include<iostream>
#include<string>
#include<stdio.h>
using namespace std;
int main()
{
	int n;
	string arr;
	bool isPositive;
	while(cin>>arr,arr!=EOF)
	{
		isPositive = true;
		n=0;
		if(arr[0]=='-')
			isPositive = false;
		if(strchr(arr,'.')!=NULL)
			n = strchr(arr,'.');
		if(n!=0)
		{
			
		}
	}
	return 0;
}