#include<iostream>
#include<algorithm>
using namespace std;
int main()
{
	int n,m,num,i,temp,dataNum=0;
	int *arr;
	cin>>n;
	while(n--)
	{
		cin>>m;
		num = m;
		arr = new int[m];
		while(m--)
		{
			cin>>arr[m];
		}
		sort(arr,arr+num);
		for(i=0;i<num;i++)
		{
			if(temp!=arr[i])
				dataNum++;
			temp = arr[i];
		}
		cout<<dataNum<<endl;
		cout<<arr[0];
		temp = arr[0];
		for(i=0;i<num;i++)
		{
			if(temp!=arr[i])
				cout<<" "<<arr[i];
			temp = arr[i];
		}
		cout<<endl;
		dataNum=0;
	}
	
	return 0;
}
