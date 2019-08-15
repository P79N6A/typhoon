#include<iostream>
using namespace std;

int main()
{
	int n,num,dayNum;
	cin>>n;
	while(n--)
	{
		cin>>num;
		if(num<10)
			dayNum=1;
		else if(num%5==0)
			dayNum=num/5-1;
		else
			dayNum=num/5;
		cout<<dayNum<<endl;
	}
	return 0;
}