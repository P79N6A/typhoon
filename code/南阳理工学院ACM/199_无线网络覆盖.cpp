#include<iostream>
#include<math.h>
using namespace std;
int main()
{
	int n,wayLong,wayWide,r;
	double m;
	cin>>n;
	while(n--)
	{
		cin>>wayLong>>wayWide>>r;
		if(wayWide/2>=r)
			cout<<"impossible"<<endl;
		else
		{
			m = wayLong/sqrt(4*r*r-wayWide*wayWide);
			cout<<ceil(m)<<endl;
		}
	}
	return 0;
} 