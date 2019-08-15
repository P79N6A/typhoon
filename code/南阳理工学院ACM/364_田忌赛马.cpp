#include<stdio.h>
#include<algorithm>
using namespace std;
int arr1[1000],arr2[1000];
bool compare(int one,int two)
{
	return one>two;
}
int main()
{
	int n,num,i,j,he;
	while(scanf("%d",&n)!=EOF)
	{
		num = 0;
		he = 0;
		for(i=0;i<n;i++)
			scanf("%d",&arr1[i]);
		for(i=0;i<n;i++)
			scanf("%d",&arr2[i]);
		sort(arr1,arr1+n);
		sort(arr2,arr2+n,compare);
		for(i=0;i<n;i++)
			for(j=0;j<n;j++)
				if(arr1[i]>arr2[j] && arr2[j]!=0 && arr1[i]!=0)
				{
					num++;
					arr2[j]=0;
					arr1[i]=0;
					break;
				}
		for(i=0;i<n;i++)
			for(j=0;j<n;j++)
				if(arr1[i]!=0 && arr2[j]!=0 && arr1[i]==arr2[j])
				{
					he++;
					arr2[j]=0;
					arr1[i]=0;
					break;
				}
		printf("%d\n",(2*num+he-n)*200);
	}
	return 0;
}