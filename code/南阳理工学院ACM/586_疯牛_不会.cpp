//1.二分法
//2.贪心算法
#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstring>
#include<cstdlib>
#include<algorithm>
#define Mx 100000
using namespace std;

int pos[Mx],n,c;

int judge(int x)//判断试探的答案是否符合条件
{
	int ab = 1;
	int ac = pos[0];//第一个默认是选定的
	for(int i=1;i<n;i++)
	{
		if(pos[i]-ac>=x)
		{
			ac = pos[i];
			ab++;
		}
	}
	if(ab >= c)//至少可以分出c个
		return 1;
	else
		return 0;
}

int search()//试探地二分枚举答案,范围0~pos[n-1]-pos[0]
{
	int left=0;
	int mid;
	int right = pos[n-1]-pos[0];
	while(left <= right)
	{
		mid = (left + right)/2;
		if(judge(mid))
			left = mid+1;
		else
			right = mid-1;
	}
	return right;//返回最终的结果
}

int main()
{
	while(scanf("%d%d",&n,&c)!=EOF)
	{
		for(int i=0;i<n;i++)
		{
			scanf("%d",&pos[i]);
		}
		sort(pos,pos+n);
		int ck = search();
		printf("%d\n",ck);
	}
	return 0;
}