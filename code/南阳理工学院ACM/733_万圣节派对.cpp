#include<stdio.h>//题目比较坑 看清楚再A
#include<math.h>

int main()
{
	int n,i,j,x,y,flag,a[10];//flag判断输出
	scanf("%d",&n);
	while(n--)
	{
		scanf("%d %d",&x,&y);
		for(i=x; i<=y; i++)
		{
			flag=0;
			a[0]=i/100000;//将整数填进数组
			a[1]=i/10000%10;
			a[2]=i/1000%10;
			a[3]=i/100%10;
			a[4]=i/10%10;
			a[5]=i%10;
			for(j=0; j<6; j++)//判断这个数中有无大于6的数
				if(a[j]>6)
				{
					flag=1;
					break;
				}
			for(j=0; j<4; j++)//判断有无三个连续数相等
				if(a[j]==a[j+1]&&a[j]==a[j+2])
				{
					flag=1;
					break;
				}
			for(j=0; j<5; j++)//判断相邻两个数差是否小于4
				if(fabs(a[j]-a[j+1])>4)
				{
					flag=1;
					break;
				}
			if(flag==0)//控制输出
			{
				for(j=0; j<6; j++)
					printf("%d",a[j]);
				printf("\n");
				}
			}
		printf("\n");
	}
	return 0;
}