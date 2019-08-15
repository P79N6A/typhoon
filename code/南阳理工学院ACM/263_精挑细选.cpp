#include<iostream>
#include<algorithm>
using namespace std;

struct Student
{  
     int length;  
     int ply;  
	 int id;  
};
  
bool cmp(Student x,Student y)
{
	if(x.length != y.length) 
		return x.length > y.length;
	if(x.ply != y.ply) 
		return x.ply < y.ply;
	return x.id > y.id;
}

int main()
{
	int n,m,i;
	cin>>n;
	while(n--)
	{
		cin>>m;
		struct Student * students = new Student[m];
		for(i=0;i<m;i++)
		{
			cin>>students[i].length;
			cin>>students[i].ply;
			cin>>students[i].id;
		}
		sort(students,students+m,cmp);
		cout<<students[0].id<<endl;
	}
}