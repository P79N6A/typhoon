#include<iostream>
using namespace std;
int main()
{
	int n,m;
	char arr;
	cin>>n;
	while(n--)
	{
		cin>>arr;
		cin>>m;
		if(arr>'Z')
			cout<<m-(arr-96)<<endl;
		else
			cout<<arr+m-64<<endl;
	}
}