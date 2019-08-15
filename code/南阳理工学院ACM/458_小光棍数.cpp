#include<iostream>
using namespace std;

int main()
{
	int n;
	long long m;
	cin>>n;
	while(n--)
	{
		cin>>m;
		if(m==0)
			cout<<0;
		else if(m==1)
			cout<<"471";
		else
			cout<<m-1<<"471";
		cout<<endl;
	}
	return 0;
}