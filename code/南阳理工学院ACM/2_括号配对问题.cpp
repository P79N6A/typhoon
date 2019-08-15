#include<iostream>
#include<stack>
#include<string>
using namespace std;

bool IsDuichen(string s);

int main()
{	
	int n;
	cin >>n;
	string *s = new string[n];
	
	for(int i=0;i < n;i++)
	{
		cin >>s[i];
	}
	
	for(int i=0;i < n;i++)
	{
		if(IsDuichen(s[i]))
		{
			if(i != n-1)
			{
				cout <<"Yes"<< endl;
			}
			else
			{
				cout <<"Yes";
			}
		}
		else
		{
			if(i != n-1)
			{
				cout <<"No"<< endl;
			}
			else
			{
				cout <<"No";
			}
		}
	}
	return 0;
}

bool IsDuichen(string s)
{
	stack<char> stk;
	for(int i=0;i < s.length();i++)
	{
		if(s[i] == '(' || s[i] == '[')
		{
			stk.push(s[i]);
		}
		else 
		{
			if(!stk.empty())
			{
				if((stk.top()=='[' && s[i]==']')||(stk.top()=='(' && s[i]==')'))
				{
					stk.pop();
				} 
				else
				{
					return false;
				}
			}
			else
			{
				return false;
			}
		}
	}
	if(stk.size() == 0)
	{
		return true;
	}
	else
	{
		return false;
	}
}


//#include<stack>
//stack<int> stk;         栈的声明 
//s.empty()               如果栈为空返回true，否则返回false  
//s.size()                返回栈中元素的个数  
//s.pop()                 删除栈顶元素但不返回其值  
//s.top()                 返回栈顶的元素，但不删除该元素  
//s.push()                在栈顶压入新元素  


