#include<iostream>
#include<algorithm>

using namespace std;

int GetMin(int n);
int GetMax(int n);
int Problem6174(int n);

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
		cout<<Problem6174(arr[i])<<endl;
	}
	return 0;
}

int Problem6174(int n)
{
	int i=0;
	int t=0;
	while(t!=n)
	{
		i++;
		t = n;
		n = GetMax(n) - GetMin(n);
	}
	return i;
}

int GetMax(int n)
{
	int *arr = new int[4];
	arr[0] = n / 1000;
	arr[1] = n / 100 - arr[0] * 10;
	arr[2] = n % 100 /10;
	arr[3] = n % 10;
	sort(arr,arr + 4);
	return arr[3] * 1000 + arr[2] * 100 + arr[1] * 10 + arr[0];
}

int GetMin(int n)
{
	int *arr = new int[4];
	arr[0] = n / 1000;
	arr[1] = n / 100 - arr[0] * 10;
	arr[2] = n % 100 /10;
	arr[3] = n % 10;
	sort(arr,arr + 4);
	return arr[0] * 1000 + arr[1] * 100 + arr[2] * 10 + arr[3];
}