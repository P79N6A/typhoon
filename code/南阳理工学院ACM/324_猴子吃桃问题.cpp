#include<iostream>
#include<string>
#include <sstream>
#include <stdlib.h>
#include<math.h>

using namespace std;

int main()
{	
	int i,j,n,sum;
	cin>>n;
	int *arr = new int[n];
	for(i = 0;i<n;i++)
	{
		cin>>arr[i];
	}
	for(i = 0;i<n;i++)
	{
		sum = 1;
		for(j = 0;j<arr[i];j++)
		{
			sum = (sum + 1) * 2;
		}
		cout<<sum<<endl;
	}
	return 0;
}