#include<iostream>
#include<math.h>
using namespace std;

int Binary(int num);

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
		cout<<Binary(arr[i])<<endl;
	}
	return 0;
}

int Binary(int num)
{
	int i;
	int sum=0;
	for(i=0 ; num >= (int)pow(2,i); i++)
	{
		if((num/(int)pow(2,i))%2==1)
		{
			num -= (int)pow(2,i);
			sum++;
		}
	}
	return sum;
}

