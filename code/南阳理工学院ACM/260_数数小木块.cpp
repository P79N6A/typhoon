#include<iostream>
using namespace std;

int main()
{
	int n,num,i=1,sum=0;
	cin>>n;
	while(n--)
	{
		cin>>num;
		for(i=1;i<=num;i++)
		{
			sum += i*(num-i);
		}
		sum += (1+num)*num/2;
		cout<<sum<<endl;
		sum=0;
	}
	return 0;
}