#include<iostream>
#include<string>
#include<sstream>
#include<math.h>

using namespace std;

string IntToString(int n);
int ZhuanHua(int num);

int main()
{
	int i,m;
	cin>>m;
	int *arr = new int[m];
	for(i=0;i<m;i++)
	{
		cin>>arr[i];
	}
	for(i=0;i<m;i++)
	{
		cout<<ZhuanHua(arr[i])<<endl;
	}
	return 0;
}

int ZhuanHua(int num)
{
	int i;
	int sum = 0;
	string numString = IntToString(num);
	int l = numString.length();
	for(i = 1 ;i < l ;i++)
	{
		sum += (int)(numString[i]-'0') * pow(10, l-i-1);
	}
	return sum;
}

string IntToString(int n)
{
    ostringstream oss;//用于向string写入,和cout<<一样，仅仅重载了<<
    oss<<n;
    string str=oss.str();
    return str;
}

