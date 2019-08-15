#include<stdio.h>
int IsBissextile(int year)
{
	if(year%400==0||(year%100!=0 && year%4==0))
		return 366;
	return 365;
}
int main()
{
	int n,year,month,day,i,dayNum;
	scanf("%d",&n);
	while(n--)
	{
		dayNum = 0;
		scanf("%d-%d-%d",&year,&month,&day);
		if(month==2 && day==29 && IsBissextile(year+20)==365)
		{
			printf("%d\n",-1);
			continue;
		}
		for(i=year+1;i<year+20;i++)
			dayNum += IsBissextile(i);
		if(month==2&&day<29 || month==1)
			dayNum += IsBissextile(year);
		else
			dayNum += IsBissextile(year+20);
		printf("%d\n",dayNum);
	}
	return 0;
}
