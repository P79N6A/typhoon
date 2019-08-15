#include<iostream>
#include<string>
using namespace std;
int main()
{
	int position,i,n;
	string arr;
	cin>>n;
	while(n--)
	{
		cin>>arr;
		position = arr.length();
		while(position%2 == 0)
		{
			for(i=0;i<position/2;i++)
				if(arr[i]!=arr[position-i-1])
					break;
			if(position/2 == i)
				position = position/2;
			else
				break;
		}
		cout<<position<<endl;
	}
}
