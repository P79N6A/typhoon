#include<iostream>
#include<cmath>

using namespace std;

bool IsNarcissisticNum(int num);

int main()
{
	int i,j;
	int *arr = new int[1000];
	for(i=0;i<1000;i++)
	{
		cin>>arr[i];
		if(arr[i]==0)
		{
			break;
		}
	}
	for(j=0;j<i;j++)
	{
		if(IsNarcissisticNum(arr[j]))
		{
			cout<<"Yes"<<endl;
		}
		else
		{
			cout<<"No"<<endl;
		}
	}
	return 0;
}

//判断数是否为水仙花数
bool IsNarcissisticNum(int num)
{
	int bai = num/100;
	int ge = num%10;
	int shi = num/10-bai*10;
	int sum = pow(ge, 3) + pow(shi, 3) + pow(bai, 3);
	
	if(sum == num)
	{
		return true;
	}
	else
	{
		return false;
	}
}