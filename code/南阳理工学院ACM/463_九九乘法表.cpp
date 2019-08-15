#include<iostream>
using namespace std;
int main()
{
	int n,i,j,t;
	cin>>n;
	int *arr = new int[n];
	for(i=0;i<n;i++)
	{
		cin>>arr[i];
	}
	for(i=0;i<n;i++)
	{
		for(j=1;j<=arr[i];j++)
		{
			for(t=j;t<=9;t++)
			{
				cout<<j<<"*"<<t<<"="<<j*t<<" ";
			}
			cout<<endl;
		}
		cout<<endl;
		cout<<endl;
	}
	return 0;
}
