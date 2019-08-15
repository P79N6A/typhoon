#include<iostream>
using namespace std;
int GetSum(int m)
{
	int i,sum=0;
	for(i=1;i<=m;i++)
		sum += i*(2+i)*(i+1)/2;
	return sum;
}
int main()
{
	int n,m,i=1;
	cin>>n;
	while(n--)
	{
		cin>>m;
		cout<<i++<<" "<<m<<" "<<GetSum(m)<<endl;
	}
	return 0;
} 