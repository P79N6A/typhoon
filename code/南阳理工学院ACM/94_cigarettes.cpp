#include<iostream>
using namespace std;

int JiSuan(int n,int k);

int main()
{
	int i,j,n,sum;
	cin>>n;
	int **arr = new int*[n];
	for(i=0;i<n;i++)
	{
		arr[i] = new int[2];
		cin>>arr[i][0];
		cin>>arr[i][1];
	}
	
	for(i=0;i<n;i++)
	{
		cout<<JiSuan(arr[i][0],arr[i][1])<<endl;
	}
	return 0;
}

int JiSuan(int n,int k)
{
	int sum = 0;
	sum = n;
	while(n/k > 0)
	{
		sum += n/k;
		n = n/k + n%k;
	}
	return sum;
}

