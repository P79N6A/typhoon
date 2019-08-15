#include<iostream>
#include<math.h>
#include<stdio.h>

using namespace std;
int main()
{
	int one, two;
	while(scanf("%d%d",&one,&two)!=EOF)
	{
		if(!one || !two)
			cout<<"Signs can't be sure"<<endl;
		else if(fabs(one)-one && !(fabs(two)-two)||!(fabs(one)-one) && fabs(two)-two)
			cout<<"Signs are opposite"<<endl;
		else
			cout<<"Signs are not opposot"<<endl;
	}
	return 0;
}
