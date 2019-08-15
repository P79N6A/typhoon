#include<iostream>
#include<queue> 

using namespace std;
int main()
{
	queue<int> q;
	int n=1,i,max=0;
	while(n!=0)
	{
		cin>>n;
		if(n!=0)
		{
			int **arr = new int*[n];
			for(i=0;i<n;i++)
			{
				arr[i] = new int[2];
				cin>>arr[i][0];
				cin>>arr[i][1];
			}
			for(i=0;i<n;i++)
			{
				if(max<arr[i][0]+arr[i][1])
				{
					max = arr[i][0]+arr[i][1];
				}
			}
			q.push(max);
			max=0;
		}
	}
	while(!q.empty())
	{
		cout<<q.front()<<endl;
		q.pop();
	}
	return 0;
}