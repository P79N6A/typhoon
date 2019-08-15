#include<iostream>
#include<string>
using namespace std;
int main()
{
	int n,i,j;
	cin>>n;
	string *arr = new string[n];
	
	for(i=0;i<n;i++)
	{
		cin>>arr[i];
	}
	for(i=0;i<n;i++)
	{
		for(j=0;j<arr[i].length();j++)
		{
			if(65 <= arr[i][j] && arr[i][j] <= 90)
				arr[i][j] += 32;
			else
				arr[i][j] = arr[i][j]-32;
			cout<<arr[i][j];
		}
		cout<<endl;
	}
	return 0;
}
