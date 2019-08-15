#include<iostream>
#include<algorithm>
using namespace std;
bool compare(int *a,int *b)
{
  return a[0]>b[0];
}
int main()
{
	int n,m,s,i,sum;
	int **arr;
	cin>>n;
	while(n--)
	{
		sum = 0;
		cin>>s>>m;
		arr = new int *[s];
		for(i=0;i<s;i++)
		{
			arr[i] = new int[2];
			cin>>arr[i][0]>>arr[i][1];
		}
		sort(arr,arr+s,compare);
		for(i=0;i<s;i++)
			if(arr[i][1]<=m)
			{
				sum += arr[i][0]*arr[i][1];
				m -= arr[i][1];
			}
			else
			{
				sum += arr[i][0]*m;
				break;
			}
		cout<<sum<<endl;
	}
	return 0;
}