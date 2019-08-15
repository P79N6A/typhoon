#include<iostream>
#include<algorithm>
#include<math.h>
using namespace std;

bool compare(int *a,int *b)
{
	return a[1]<b[1];
}

int main()
{
	int **arr;
	int num,i,n,m,N;
	cin>>N;
	while(N--)
	{
		num = 0;
		m = 0;
		cin>>n;
		arr = new int *[n];
		for(i=0;i<n;i++)
		{
			arr[i] = new int[2];
			cin>>arr[i][0]>>arr[i][1];
		}
		sort(arr,arr+n,compare);
		for(i=0;i<n;i++)
			if(m<arr[i][0])
			{
				num++;
				m = arr[i][1];
			}
		cout<<num<<endl;
	}
	return 0;
}