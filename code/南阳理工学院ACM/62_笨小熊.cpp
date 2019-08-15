#include<iostream>
#include<string>
#include<math.h>
using namespace std;

int MaxnMinn(string word);
bool IsPrime(int num);

int main()
{
	int i,n,sum;
	cin>>n;
	string *arr = new string[n];
	for(i=0;i<n;i++)
	{
		cin>>arr[i];
	}
	for(i=0;i<n;i++)
	{
		sum = MaxnMinn(arr[i]);
		if(IsPrime(sum))
		{
			cout<<"Lucky Word"<<endl;
			cout<<sum<<endl;
		}
		else
		{
			cout<<"No Answer"<<endl;
			cout<<0<<endl;
		}
		
	}
	return 0;
}

int MaxnMinn(string word)
{
	int i,j,max=0,min=word.length(),sum;
	char temp;
	for(i=0;i<word.length();i++)
	{
		temp = word[i];
		sum = 0;
		for(j=0;j<word.length();j++)
		{
			if(temp == word[j])
			{
				sum++;
			}
		}
		if(sum>max)
		{
			max = sum;
		}
		if(sum<min)
		{
			min = sum;
		}
	}
	return max - min;
}

//是否是素数
bool IsPrime(int n)
{
	int i;
	if(n==1 || n==0)
	{
		return false;
	}
	for(i=2;i<=sqrt(n);i++)
	{
		if(n%i==0)
		{
			return false;
		}
	}
    return true;
}




