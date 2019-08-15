#include<iostream>
#include<math.h>
using namespace std;
int main()
{
	int n,m,i,sum;
	cin>>n;
	while(n--)
	{
		sum = 0;
		cin>>m;
		m = m+1;
		int b = (int)(sqrt(m)+0.5);
		for(int i=2;i<=b;i++) 
			if(m%i==0)
				sum++;
		cout<<sum<<endl;
	}
	return 0;
}