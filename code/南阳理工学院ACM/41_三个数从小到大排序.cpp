#include<iostream>
#include<algorithm>

using namespace std;

int main()
{
	int i,m;
	int *arr = new int[3];
	for(i=0;i<3;i++)
	{
		cin>>arr[i];
	}
	sort(arr,arr+3);
	for(i=0;i<3;i++)
	{
		cout<<arr[i]<<" ";
	}
	return 0;
}


