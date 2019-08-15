#include<stdio.h>
#include<string.h>
#include<iostream>
using namespace std;
int main()
{
	int N,i;
	string temp;
	while(scanf("%d",&N) != EOF)
	{
		for(i=0;i<N;i++)
		{
			cin>>temp;
			if(temp == "bowl"||temp == "knife"||temp == "fork"||temp == "chopsticks")
				cout<<temp<<" ";
		}
		cout<<endl;
	}
	return 0;
}        