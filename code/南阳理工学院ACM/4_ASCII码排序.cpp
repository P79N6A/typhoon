#include<iostream>
#include<string>
#include <algorithm>

using namespace std;
int main()
{
	int row;
	cin>>row;
	string* arr = new string[row];
	for(int i=0;i<row;i++)
	{
		cin>>arr[i];
		sort(arr[i].begin(),arr[i].end());
	}
	for(int i=0;i<row;i++)
	{
		for(int j=0;j<arr[i].length();j++)
		{
			cout<<arr[i][j]<<" ";
		}
		cout<<endl;
	}
	return 0;
}