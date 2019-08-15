#include <iostream>
#include <math.h>
using namespace std;

int PrimeNum(int arr[]);

int main()
{
	int n,num,i,j;
	cin>>n;
	int **arr = new int*[n];
	for(i=0;i<n;i++)
	{
		cin>>num;
		arr[i] = new int[num+1];
		arr[i][0] = num;
		for(j=1;j < num+1;j++)
		{
			cin>>arr[i][j];
		}
	}
	for(i=0;i<n;i++)
	{
		cout<<PrimeNum(arr[i])<<endl;
	}
	return 0;
}

//输出数组素数数目
int PrimeNum(int arr[])
{
	int n = 0;
	int m,i;
	for(i=1;i<=arr[0];i++)
	{
		if(arr[i] == 2)
		{
			n += arr[i];
			
		}
		else if(arr[i] == 1)
		{}
		else
		{
			for(m = 2; m <= (int)sqrt((double)arr[i])+1; m++)
			{
				if(arr[i]%m == 0)break;
			}	
			if(m > (int)sqrt((double)arr[i]))
			{
				n += arr[i];
			}
		}
	}
	return n;
}