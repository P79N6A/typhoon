#include<iostream>
#include<math.h>
using namespace std;

void LightUp(int n,int k);

int main()
{
	int i;
	int n,k;
	cin>>n;
	cin>>k;
	LightUp(n,k);
	return 0;
}

void LightUp(int n,int k)
{
	int *arr = new int[n+1];
	int i,j,t;
	for(i=0;i<=n;i++)
	{
		arr[i] = 0;
	}
	if(k > 0)
	{
		for(i=0;i<=n;i++)
		{
			arr[i] = 1;
		}
		for(i=2;i<=k;i++)
		{	
			int pos=i;
			while(pos<=n)
			{
				if(arr[pos]==1)
				{
					arr[pos]=0;
				}
				else
				{
					arr[pos]=1;
				}
				pos+=i;     //找到所有的倍数
			}
		}
	}
	for(i=1;i<=n;i++)
	{
		if(arr[i]==1)
		{
			cout<<i<<" ";
		}
	}
}

