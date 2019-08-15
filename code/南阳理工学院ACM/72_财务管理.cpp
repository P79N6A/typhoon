#include<iostream>
#include<algorithm>

using namespace std;

int main()
{
	int i,m;
	double sum = 0;
	double *arr = new double[12];
	for(i=0;i<12;i++)
	{
		cin>>arr[i];
		sum += arr[i];
	}
	sum = sum/12;
	cout.precision(2);
	cout.setf(ios::fixed);
	cout<<sum;
	return 0;
}


