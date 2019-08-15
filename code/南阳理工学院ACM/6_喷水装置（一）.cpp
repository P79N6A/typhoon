#include<iostream>
#include<algorithm>
#include<math.h>
using namespace std;
bool compare(double a,double b)
{
  return a>b;
}
int main()
{
	int n,s,i,sum;
	double m;
	double *arr;
	cin>>n;
	while(n--)
	{
		m = 20;
		sum = 0;
		cin>>s;
		arr = new double[s];
		for(i=0;i<s;i++)
			cin>>arr[i];
		sort(arr,arr+s,compare);
		for(i=0;i<s;i++)
			if(m>0)
			{
				m -= sqrt(arr[i]*arr[i]-1)*2;
				sum++;
			}
			else
				break;
		cout<<sum<<endl;
	}
	return 0;
}