#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{
	int n;
	cin>>n;
	while(n--)
	{
		double m,x,y,z;
		cin>>m>>x>>y>>z;
		printf("%.2lf\n",(m*x)/(y-x)*z);
	}
	return 0;
}