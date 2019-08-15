#include<iostream>
using namespace std;
int main()
{
	int n,m,i,j,sum,max;
	int **arr;
	cin>>n;
	while(n--)
	{
		cin>>m;
		arr = new int*[m];
		for(i=0;i<m;i++)
		{
			arr[i] = new int[3];
			cin>>arr[i][0]>>arr[i][1]>>arr[i][2];
		}
		max = 0;
		for(i=1;i<=180;i++)
		{
			sum = 0;
			for(j=0;j<m;j++)
				if(arr[j][1]<=i && i< arr[j][1] + arr[j][2])
					sum += arr[j][0];
			if(max<sum)
				max = sum;
		}
		cout<<max<<endl;
	}
	return 0;
}