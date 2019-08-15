#include<iostream>
#include <math.h>
using namespace std;

bool IsPrime(int num);

int main()
{
	int n,i,j;
	cin>>n;
	int *arr = new int[n];
	for(i = 0;i<n;i++)
	{
		cin>>arr[i];
	}
	for(i = 0;i<n;i++)
	{
		for(j = 0;j<=n;j++)
		{
			if(IsPrime(arr[i] + j))
			{
				cout<<arr[i] + j<<endl;
				break;
			}
			if((arr[i]-j)>0 && IsPrime(arr[i]-j))
			{
				cout<<arr[i] - j<<endl;
				break;
			}
		}
	}
	return 0;
}

//是否是素数
bool IsPrime(int n)
{
	int i;
	if(n==1 || n==0)
	{
		return false;
	}
	for(i=2;i<=sqrt(n);i++)
	{
		if(n%i==0)
		{
			return false;
		}
	}
    return true;
}