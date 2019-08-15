#include <iostream>
using namespace std;

int main()
{
	int n,i,min,minSign,t;
	int *arr;
	char one,two;
	while(n)
	{
		cin>>n;
		if(n)
		{
			arr = new int[n];
			for(i=0;i<n;i++)
				cin>>arr[i];
			min=arr[0];
			minSign=0;
			for(i=1;i<n;i++)
			{
				if(min>arr[i])
				{
					min=arr[i];
					minSign=i; 
				}
			}
			t=arr[0];
			arr[0]=arr[minSign];
			arr[minSign]=t;
			for(i=0;i<n;i++)
				cout<<arr[i]<<" ";
			cout<<endl;
		}
	}
} 