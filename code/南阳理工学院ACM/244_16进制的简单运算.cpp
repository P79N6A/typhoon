#include <stdio.h>
int main()
{
	int n;
	scanf("%d",&n);
	while(n--)
	{
		int a,b;
		char ch;
		scanf("%x%c%x",&a,&ch,&b);
		printf("%o\n",ch=='+'?a+b:a-b);
	}
}