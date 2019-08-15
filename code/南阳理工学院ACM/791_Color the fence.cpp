/*
这道题的解法就是在保证长度最长的前提下，让首位尽可能的大
，所以用v/最小值，再用v%最小值，然后在余数允许的范围内让
其他位的值尽可能的大(波动增大)
 */
#include<stdio.h>
int main()
{
	int n,i,id,digit,remainder,now;
	int arr[9];
	while(scanf("%d",&n)!=EOF)
	{
		for(i=0;i<9;i++)
			scanf("%d",&arr[i]);
		id = 0;
		for(i=1;i<9;i++)
			if(arr[i] <= arr[id])
				id = i;
		digit = n/arr[id];
		remainder = n%arr[id];
		while(digit--)
		{
			now = id;
			for(i=8;i>id;i--)
				if(arr[i]-arr[id] <= remainder)
				{
					now = i;
					remainder -= (arr[i]-arr[id]);
					break;
				}
			printf("%d",now+1);
		}	
		printf("\n");
	}
	return 0;
}