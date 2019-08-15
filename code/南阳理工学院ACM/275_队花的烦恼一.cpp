#include<stdio.h>
int main()
{
	int a,i;
	while(scanf("%d",&a)!=EOF)
	{
		if(a<2)
			printf("%d\n",a);
		else
		{
			int b[30];
			for(i=0;a>0;i++)
			{
				b[i]=a%2;
				a=a/2;
			}
			while(i>0)
				printf("%d",b[--i]);	
			printf("\n");
		} 
	}
	return 0;
} 
