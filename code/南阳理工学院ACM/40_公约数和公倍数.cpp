#include<iostream>
using namespace std;

int Gcd(int one, int two);
int LCM(int one, int two);

int main()
{
	int i;
	int n;
	cin>>n;
	int **arr = new int*[n];
	for(i=0;i<n;i++)
	{
		arr[i] = new int[2];
		cin>>arr[i][0]>>arr[i][1];
	}
	for(i=0;i<n;i++)
	{
		cout<<Gcd(arr[i][0], arr[i][1])<<" "<<LCM(arr[i][0], arr[i][1])<<endl;
	}
	return 0;
}

//最大公约数
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

int gcd(int a,int b)
{
	if(a==0) return b;
	else return gcd(b%a,a);
}

//最小公倍数
int LCM(int one, int two)
{
	return one * two / Gcd(one, two);
}