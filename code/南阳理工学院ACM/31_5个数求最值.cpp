#include<iostream>
using namespace std;
int main()
{
	int i;
	int min,max;
	int *arr = new int[5];
	for(i=0;i<5;i++)
	{
		cin>>arr[i];
	}
	min = arr[0];
	max = arr[0];
	for(i=1;i<5;i++)
	{
		if(min > arr[i])
		{
			min = arr[i];
		}
		if(max < arr[i])
		{
			max = arr[i];
		}
	}
	cout<<min<<" "<<max<<endl;
	return 0;
}