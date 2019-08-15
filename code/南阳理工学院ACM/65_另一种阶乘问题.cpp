#include<iostream>
using namespace std;

int Factorial(int n);

int main()
{
	int i;
	int n;
	cin>>n;
	int *arr = new int[n];
	for(i=0;i<n;i++)
	{
		cin>>arr[i];
	}
	for(i=0;i<n;i++)
	{
		cout<<Factorial(arr[i])<<endl;
	}
	return 0;
}

int Factorial(int n)
{
	int i,j;
	int sum = 0;
	int product = 1;
	for(i=1;i<=n;i++)
	{
		for(j=1;j<=i;j++)
		{
			if(j%2==1)
			{
				product *= j;
			}
		}
		sum += product;
		product = 1;
	}
	return sum;
}

