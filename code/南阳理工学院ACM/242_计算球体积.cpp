#include <stdio.h>
#define PI 3.1415926
int main()
{
	double r;
	while(~scanf("%lf",&r))
	{
		printf("%.lf\n",PI*r*r*r*4/3);
	}
} 