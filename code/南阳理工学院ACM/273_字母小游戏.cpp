#include<iostream>
#include<string>
using namespace std;
int main()
{
	int n,i,j,max=0,maxSign=0;
	cin>>n;
	string *arr = new string[n];
	int *letterNum = new int[26]();
	for(i=0;i<n;i++)
		cin>>arr[i];
	for(i=0;i<n;i++)
	{
		for(j=0;j<26;j++)
		{
			letterNum[j]=0;
		}
		for(j=0;j<arr[i].length();j++)
		{
			letterNum[arr[i][j]-'a']++;
		}
		if(arr[i].length()>0)
		{
			max = letterNum[0];
			maxSign=0;
		}
		for(j=0;j<26;j++)
		{
			if(letterNum[j]!=0 && max==0)
			{
				max = letterNum[j];
				maxSign = j;
			}
			if(max<letterNum[j] && letterNum[j]!=0)
			{
				max = letterNum[j];
				maxSign = j;
			}
		}
		cout<<char(maxSign+'a')<<endl;
	}
	return 0;
}