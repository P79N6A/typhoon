#include<iostream>
using namespace std;

int JiSuan(int n,int m);

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

int JiSuan(int n,int m)
{
	int i,t,sum=0;
	for(i=1;i<=n;i++)
	{
		t=i;
		while(t%m==0)
		{
			sum++;
			t=t/m;
		}
	}
	return sum;
}

