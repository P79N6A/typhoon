#include<iostream>
#include<algorithm>
#include<math.h>
using namespace std;

bool compare(double *a,double *b)
{
  return a[1]>b[1];
}

int main()
{
	double w,h,N,temp;
	double m;
	double **arr;
	int num,i,n;
	cin>>N;
	bool isChange;
	while(N--)
	{
		num = 0;
		m = 0;
		cin>>n>>w>>h;
		h=h/2;
		arr = new double *[n];
		for(i=0;i<n;i++)
		{
			arr[i] = new double[2];
			cin>>arr[i][0]>>arr[i][1];
			if(arr[i][1]>h)
			{
				temp = sqrt(arr[i][1]*arr[i][1]-h*h);
				arr[i][1] = temp + arr[i][0];
				arr[i][0] -= temp;
			}
			else
				arr[i][1] = 0;
		}
		sort(arr,arr+n,compare);
		while(m<w)
		{
			isChange = false;
			for(i=0;i<n;i++)
				if(arr[i][0]<=m && arr[i][1]>0)
				{
					isChange = true;
					num++;
					m = arr[i][1];
					arr[i][1] = 0;
					break;
				}
			if(!isChange)
			{
				num = 0;
				break;
			}
		}
		cout<<num<<endl;
	}
	return 0;
}        