#include <stdio.h>
#include <string.h>
int num[1000001]={0};
int num2[1000001]={0};
char temp[20];
int main()
{
	for(int i=125;i<=1000000;i++)
	{
		sprintf(temp,"%d",i);
		if(strstr(temp,"521")!=NULL)
			num2[i]=num2[i-1]+1;
		else
			num2[i]=num2[i-1];
		if(strchr(temp,'5')==NULL||strchr(temp,'2')==NULL||strchr(temp,'1')==NULL)
			num[i] = num[i-1];
		else
			num[i]=num[i-1]+1;
	}	
	int x,y;
	int caseNum=1;
	while(~scanf("%d%d",&x,&y))
		printf("Case %d:%d %d\n",caseNum++,num[y]-num[x-1],num2[y]-num2[x-1]);
}