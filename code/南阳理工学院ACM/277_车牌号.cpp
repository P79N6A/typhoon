#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main()
{
	int n,i,m,j;
	string *arr;
	cin>>n;
	for(i=0;i<n;i++)
	{
		cin>>m;
		arr = new string[m];
		for(j=0;j<m;j++)
		{
			cin>>arr[j];
		}
		sort(arr,arr+m);
		cout<<arr[0]<<endl;
	}
} 