#include<iostream>
#include<string>
using namespace std;
int main()
{
	int n,i=1;
	string arr;
	cin>>n;
	while(n--)
	{
		cin>>arr;
		for(i=arr.length()-1;i>=0;i--)
			switch(arr[i])
			{
				case '0':cout<<"O";break;
				case '1':cout<<"O";break;
				case '2':cout<<"T";break;
				case '3':cout<<"T";break;
				case '4':cout<<"F";break;
				case '5':cout<<"F";break;
				case '6':cout<<"S";break;
				case '7':cout<<"S";break;
				case '8':cout<<"E";break;
				case '9':cout<<"N";break;
			}
		cout<<endl;
	}
	return 0;
} 