#include<stdio.h>
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
void ZhiHuan(int **arr,int n)
{
	int i;
	int x = -1,y = 0;//初始坐标位置
	int direction = 2;//上:1,右:2,下:3,左:4
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
int main()
{
	int n,i,j,sum;
	int **arr;
	while(scanf("%d",&n)!=EOF)
	{	
		sum = 0;
		arr = new int*[n];
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
			sum += arr[i][n-i-1];
		printf("%d\n",sum);
	}
	return 0;
}

