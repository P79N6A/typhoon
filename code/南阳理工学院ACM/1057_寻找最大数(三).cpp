#include<string.h>
#include<iostream>
using namespace std;
int main()
{
	string arr;
	int n,i,j,max,maxId,temp;
	while(cin>>arr>>n)
	{
		for(i=0;i<arr.length()-1 && n>0;i++)
		{
			max = arr[i];
			maxId = i;
			for(j=i+1;j<=i+n && j<arr.length();j++)
				if(max<arr[j])
				{
					max = arr[j];
					maxId = j;
				}
			n -= maxId-i;
			for(j=maxId;j!=i;j--)
			{
				temp = arr[j];
				arr[j] = arr[j-1];
				arr[j-1] = temp;
			}
		}
		cout<<arr<<endl;
	}
	return 0;
}