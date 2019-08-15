#include<iostream>
#include<string>
#include <sstream>
#include <stdlib.h>
#include<math.h>
#include<stdio.h>

using namespace std;

int LCM(int one, int two);
int Gcd(int one, int two);
string JiSuan(string arr);
string IntToString(int n);

int main()
{	
	string arr;
	while(getline(cin,arr))
	{
		cout<<JiSuan(arr)<<endl;
	}
	return 0;
}

string JiSuan(string arr)
{
	int denominatorOne = 0;
	int denominatorTwo = 0;
	int moleculeOne = 0;
	int moleculeTwo = 0;
	int multiple = 0;
	int jieGuo = 0;
	int divisor = 0;
	char oper; 
	
	int i,j;
	string temp;
	for(i=0,j=0;i<arr.length();i++)
	{
		if(arr[i]=='/')
		{
			j++;
			switch(j)
			{
				case 1:moleculeOne = atoi(temp.c_str());break;
				case 2:moleculeTwo = atoi(temp.c_str());break;
			}
			temp = "";
		}
		else if(arr[i]== '+'|| arr[i]== '-')
		{
			denominatorOne = atoi(temp.c_str());
			temp = "";
			oper = arr[i];
		}
		else if(i == arr.length()-1)
		{
			temp += arr[i];
			denominatorTwo = atoi(temp.c_str());
		}
		else
		{
			temp += arr[i];
		}
	}
	multiple = LCM(denominatorOne, denominatorTwo);
	moleculeOne = moleculeOne*multiple/denominatorOne;
	moleculeTwo = moleculeTwo*multiple/denominatorTwo;
	
	switch(oper)
	{
		case '+': jieGuo = moleculeOne + moleculeTwo; break;
		case '-': jieGuo = moleculeOne - moleculeTwo; break;
	}
	
	if(jieGuo==0)
	{
		return "0";
	}
	divisor = Gcd(fabs(jieGuo), multiple);
	
	jieGuo = jieGuo/divisor;
	multiple = multiple/divisor;
	
	if(multiple == 1)
	{
		return IntToString(jieGuo);
	}
	else
	{
		return IntToString(jieGuo) + "/" + IntToString(multiple);
	}
}

//最大公约数
int Gcd(int one, int two)
{
	int t;
	while(two!=0)
	{
		t = two;
		two = one%two;
		one = t;
	}
	return one;
}

//最小公倍数
int LCM(int one, int two)
{
	return one * two / Gcd(one, two);
}

//int转string
string IntToString(int n)
{
	stringstream ss;
    string str;
    ss<<n;
    ss>>str;
	return str;
}        