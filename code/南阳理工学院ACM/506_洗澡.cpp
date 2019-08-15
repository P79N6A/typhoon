//本题相当于把9进制数转成10进制数。
#include<stdio.h>
int main()
{
	int n,x,s,t;
	while(~scanf("%d",&n))
	{
		s=0,t=1;
		while(n)
		{
			x = n%10;
			if(x>4) 
				s += (x-1)*t;
			else 
				s += x*t;
			n /= 10;
			t *= 9;
		}
		printf("%d\n",s);
	}
	return 0;
}