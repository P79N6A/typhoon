#include<iostream>
#include<algorithm>
using namespace std;
bool cmp(string a,string b)
{
  return a.length()<b.length();
}
int main()
{
	int n,i,j=0;
	string *arr;
	while(cin>>n,n!=0)
	{
		j++;
		arr = new string[n];
		for(i=0;i<n;i++)
			cin>>arr[i];
		sort(arr,arr + n,cmp);
		cout<<"SET "<<j<<endl;
		for(i=0;i<n;i+=2)
			cout<<arr[i]<<endl;
		for(i=n-1;i>0;i=i-2)
		{
			if(i%2!=1)
				i=i-1;
			cout<<arr[i]<<endl;
		}
	}
	return 0;
}
