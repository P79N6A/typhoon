#include<iostream>
#include<string>
#include<math.h>

using namespace std;

int Gcd(int one, int two);

int main()
{
	int n,k,i;
	int u=0,d=0,s=0;
	string arr;
	cin>>n;
	cin>>arr;
	while(n--)
	{
		if(arr[n]=='U')
			u++;
		else if(arr[n]=='D')
			d++;
		else
			s++;
	}
	if(s>0)
		cout<<"Bingo";
	else if(fabs((double)u/(u+d+s)-0.5)>0.003)
		cout<<"Fail";
	else
		cout<<u/Gcd(u, u+d+s)<<"/"<<(u+d+s)/Gcd(u, u+d+s);
	return 0;
}

int Gcd(int one, int two)
{
	int t;
	while(two!=0)
	{
		t = two;
		two = one%two;
		one = t;
	}
	return one;
}