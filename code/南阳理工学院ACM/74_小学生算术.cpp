#include<iostream>
#include<string>
#include<math.h>

using namespace std;

int JinWeiNum(int one,int two);

int **arr = new int*[1000];

int main()
{
	int i;
	for(i=0;i<1000;i++)
	{
		arr[i] = new int[2];
		cin>>arr[i][0];
		cin>>arr[i][1];
		if(arr[i][0]==0 && arr[i][1]==0)break;
	}
	for(i=0;i<1000;i++)
	{
		if(arr[i][0]==0 && arr[i][1]==0)break;
		cout<<JinWeiNum(arr[i][0],arr[i][1])<<endl;
	}
	return 0;
}

int JinWeiNum(int one,int two)
{
	int onet,twot;
	int i,sum=0;
	for(i=0;i<3;i++)
	{	
		onet = one % (int)pow(10, (double)(i+1));
		twot = two % (int)pow(10, (double)(i+1));
		if(onet + twot >= pow(10, (double)(i+1)))
		{
			sum++;
		}
	}
	return sum;
}



