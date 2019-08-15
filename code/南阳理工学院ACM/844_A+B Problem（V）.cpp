#include <iostream>
#include <string>
#include<stdlib.h>  
using namespace std;

int main()
{
	int n,i;
	int *arr;
	string one,two;
	string oneTran ="";
	string twoTran ="";
	do
	{
		cin>>one;
		cin>>two;
		oneTran="";
		twoTran="";
		if(one!="0" && two!="0")
		{
			for(i=one.length()-1;i>=0;i--)
			{
				oneTran = oneTran+one[i];
			}
			for(i=two.length()-1;i>=0;i--)
			{
				twoTran = twoTran+two[i];
			}
			cout<<atoi(oneTran.c_str())+atoi(twoTran.c_str())<<endl;
		}
	}while(one!="0" && two!="0");
} 