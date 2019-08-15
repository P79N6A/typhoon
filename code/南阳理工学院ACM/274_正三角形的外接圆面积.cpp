#include<stdio.h>
#define pi 3.1415926
int main()
{ 
	int n;
	scanf("%d",&n); 
	while(n--)
	{ 
		double m,s; //提醒一下float过不了
		scanf("%lf",&m); 
		s=m*m*pi/3.0;
		printf("%.2lf\n",s);
	}
	return 0;	
}