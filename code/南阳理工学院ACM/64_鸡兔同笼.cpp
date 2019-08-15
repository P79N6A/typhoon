#include<iostream>
using namespace std;

void WODR(int n, int m);

int main()
{
	int i;
	int n;
	cin>>n;
	int **arr = new int*[n];
	for(i=0;i<n;i++)
	{
		arr[i] = new int[2];
		cin>>arr[i][0]>>arr[i][1];
	}
	for(i=0;i<n;i++)
	{
		WODR(arr[i][0], arr[i][1]);
	}
	return 0;
}

//鸡兔同笼
//1.保证chickenNum、rabbitNum为整数
//2.保证chickenNum、rabbitNum为非负数
void WODR(int n, int m)
{
	int chickenNum = (4 * n - m)/2;
	int rabbitNum = (m - 2 * n)/2;
	if(chickenNum >= 0 && rabbitNum >= 0 && (4 * n - m)%2 == 0 && (m - 2 * n)%2 == 0)
	{
		cout<<chickenNum<<" "<<rabbitNum<<endl;
	}
	else
	{
		cout<<"No answer"<<endl;
	}
}