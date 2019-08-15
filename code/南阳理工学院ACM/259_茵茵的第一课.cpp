#include<iostream>
using namespace std;
int main()
{
	int n,i,j;
	cin>>n;
	string *arr = new string[n];
	for(i = 0;i<n;i++)
	{
		cin>>arr[i];
	}
	for(i = 0;i<n;i++)
	{
		cout<<arr[i]<<endl;
	}
	return 0;
}
