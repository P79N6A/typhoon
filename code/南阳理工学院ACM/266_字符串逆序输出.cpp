#include<iostream>
#include<string>

using namespace std;

int main()
{	
	int i,j,n;
	cin>>n;
	string *arr = new string[n+1];
	for(i=0;i<n+1;i++)
	{
		getline(cin,arr[i]);
	}
	for(i=1;i<n+1;i++)
	{
		for(j=arr[i].length()-1;j>=0;j--)
		{
			if(!('0' <= arr[i][j] && arr[i][j] <= '9') && arr[i][j]!=' ')
				cout<<arr[i][j];
		}
		cout<<endl;
	}
	return 0;
}