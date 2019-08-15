#include<stdio.h>
#include<math.h>
bool IsHaveFour(int data)
{
	int i,n;
	n = (int)log10(data);
	for(i=0;i<=n;i++);
		if(data%10==4)
			return true;
		else
			data/=10;
	return false;
}
int main()
{
	if(IsHaveFour(40))
	{
		printf("%d",(int)log10(8));
	}
	return 0;
}