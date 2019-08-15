#include<iostream>
#include<string>
#include<cstdlib>
#include<math.h>

using namespace std;
int main()
{
	int n,m,i,ply,timeSum;
	cin>>n;
	string *arr;
	while(n--)
	{
		cin>>m;
		timeSum = 0;
		ply = 0;
		arr = new string[m+1];
		for(i=0;i<=m;i++)
			getline(cin,arr[i]);
		for(i=1;i<=m;i++)
		{
			if(!arr[i].compare("IN"))
				ply++;
			else if(!arr[i].compare("OUT"))
				ply--;
			else
			{
				arr[i] = arr[i].substr(5,arr[i].length()-5);
				timeSum += atoi(arr[i].c_str())*60/pow(20,ply);
			}
		}
		cout<<timeSum<<endl;
	}
	return 0;
}