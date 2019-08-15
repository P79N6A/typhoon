#include<stdio.h>
int main()
{
	char a[3],b[10];int c=1;
	while(scanf("%s %s",a,b)!=EOF)
	{
		printf("Case %d: ",c++);
		a[1]=='#'?a[0]=='G'?printf("Ab %s\n",b):printf("%cb %s\n",a[0]+1,b):
		a[1]=='b'?a[0]=='A'?printf("G# %s\n",b):printf("%c# %s\n",a[0]-1,b):printf("UNIQUE\n");	
	}
	return 0;
} 