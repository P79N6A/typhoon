/*
抽屉原理。
sum[0]=0;
sum[i]=(a[1]+a[2]+a[3]...a[i])%n;
如果存在i>0 使得sum[i]=0;则直接输出a[1],a[2],,....a[i]即可满足题意。
如果不存在，考虑sum[ j ]-sum[ i ]=a [ i+1 ],a[ i+2 ]....a[ j ]。
即如果存在sum[ j ]-sum[ i ]==0,则输出 a [ i+1 ],a[ i+2 ]....a[ j ] 即可。
接下来用抽屉原理证明 i , j 必然存在。
抽屉原理：
如果将大于n个数量的物品放入n个抽屉，则必然存在某个抽屉放了大于1个物品。
因为sum [ i ] 的值只能是1,....n-1.sum [ i ]的数量有n个。
所以由抽屉原理可知，必然存在某两个sum [ i ] 值一样。
 */
#include<stdio.h>
int arr[10000];
int sum[10000];
int main()
{
	int n,i,j;
	bool isTrue;
	while(scanf("%d",&n)!=EOF)
	{
		for(i=0;i<n;i++)
		{
			scanf("%d",&arr[i]);
			if(i != 0)
				sum[i] = (sum[i-1] + arr[i]) % n;
			else
				sum[i] = arr[i] % n;
		}
		for(i=0;i<n;i++)
		{
			if(sum[i]==0)
			{
				isTrue = true;
				break;
			}
			for(j=i+1;j<n;j++)
				if(sum[i]==sum[j])
				{
					isTrue = true;
					break;
				}
			if(isTrue)
				break;
		}
		if(isTrue)
			printf("YES\n");
		else
			printf("NO\n");
	}
	return 0;
}