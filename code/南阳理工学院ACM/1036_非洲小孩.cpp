#include<algorithm>
#include<stdio.h>
#include<string.h>
using namespace std;
typedef struct
{
	string start;
	string end;
	
}BathTime;
bool compare(BathTime a,BathTime b)
{
	if(a[1]!=b[1])
		return a[1]<b[1];
	else
		return a[0]>b[0];
}
int main()
{
	int i,N;
	BathTime *arr;
	string stringTime;
	while(scanf("%d",&N) != EOF)
	{
		arr = new BathTime[N];
		cin>>stringTime;
		sort(arr,arr + N,compare);
	}
	return 0;
}