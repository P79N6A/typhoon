#include<iostream>
#include<string>

using namespace std;
int main()
{
	int n,k,i;
	int r=0,w=0,b=0;
	string arr;
	cin>>n;
	while(n--)
	{
		cin>>arr;
		for(i=0;i<arr.length();i++)
		{
			if(arr[i]=='R')
				r++;
			else if(arr[i]=='W')
				w++;
			else
				b++;
		}
		while(r--)
			cout<<"R";
		while(w--)
			cout<<"W";
		while(b--)
			cout<<"B";
		cout<<endl;
		r=0;w=0;b=0;
	}
	return 0;
}