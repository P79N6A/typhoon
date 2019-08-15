#include<iostream>
#include<string>
#include<math.h>
using namespace std;

int ChangeDir(int direction);
void ZhiHuan(int **arr,int n);

int main()
{
	int i,j,n,sum;
	cin>>n;
	int **arr = new int*[n];
	for(i=0;i<n;i++)
	{
		arr[i] = new int[n];
		for(j=0;j<n;j++)
		{
			arr[i][j] = 0;
		}
	}
	
	ZhiHuan(arr,n);
	
	for(i=0;i<n;i++)
	{
		for(j=0;j<n;j++)
		{
			cout<<arr[i][j]<<" ";
		}
		cout<<endl;
	}
	return 0;
}

void ZhiHuan(int **arr,int n)
{
	int i;
	int x = n-1,y = -1;//初始坐标位置
	int direction = 3;//上:1,右:2,下:3,左:4
	for(i = 0;i < n*n;i++)
	{
		switch(direction)
		{
			case 1:arr[--y][x] = i+1;if(y==0|| arr[y-1][x]!=0) direction = ChangeDir(direction);break;
			case 2:arr[y][++x] = i+1;if(x==n-1|| arr[y][1+x]!=0) direction = ChangeDir(direction);break;
			case 3:arr[++y][x] = i+1;if(y==n-1|| arr[1+y][x]!=0) direction = ChangeDir(direction);break;
			case 4:arr[y][--x] = i+1;if(x==0|| arr[y][x-1]!=0) direction = ChangeDir(direction);break;
		}
	}
}


//顺时针改变方向
int ChangeDir(int direction)
{
	if(direction < 4)
	{
		direction++;
	}
	else
	{
		direction = 1;
	}
	return direction;
}




