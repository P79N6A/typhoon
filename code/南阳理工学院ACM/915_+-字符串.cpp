#include<iostream>
#include<stdio.h>
#include<string.h>
using namespace std;
int GetNum(string a)
{
	int i=0,num=0;
	for(i=0;i<a.length();i++)
		if(a[i]=='+')
			num++;
	return num;
}
int main()
{
	int i,num,j;
	bool isChange = true;
	char temp;
	string a,b;
	while(cin>>a>>b)
	{
		num=0;
		if(a.length()==b.length() && GetNum(a) == GetNum(b))
		{
			for(i=0;i < a.length()-1;i++)
				if(a[i]!=b[i])
					for(j=i+1;j < a.length();j++)
						if(a[i]!=a[j])
						{
							temp = a[i];
							a[i] = a[j];
							a[j] = temp;
							num += j-i;
							break;
						}
						
			printf("%d\n",num);
		}
		else
			printf("%d\n",-1);
	}
	return 0;
}

