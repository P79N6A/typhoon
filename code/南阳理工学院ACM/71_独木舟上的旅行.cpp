#include<iostream>
#include<algorithm>
using namespace std;
int main()
{
	int *arr;
	int num,i,n,w,N,j;
	cin>>N;
	while(N--)
	{
		num = 0;
		cin>>w>>n;
		arr = new int[n];
		for(i=0;i<n;i++)
			cin>>arr[i];
		sort(arr,arr + n);
		i = 0;
		j = n-1;
		while(i<=j)
		{
			if(arr[i]+arr[j]<=w)
			{
				i++;
				j--;
			}
			else
				j--;
			num++;
		}
		cout<<num<<endl;
	}
	return 0;
}