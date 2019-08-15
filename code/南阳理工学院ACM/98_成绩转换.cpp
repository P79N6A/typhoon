#include<iostream>

using namespace std;

char Rate(int score);

int main()
{
	int i,m;
	int sum = 0;
	cin>>m;
	int *arr = new int[m];
	for(i=0;i<m;i++)
	{
		cin>>arr[i];
	}
	for(i=0;i<m;i++)
	{
		cout<<Rate(arr[i])<<endl;
	}
	return 0;
}

char Rate(int score)
{
	char grade;
	if(90<=score && score<=100)
		grade = 'A';
	else if(80<=score && score<=89)
		grade = 'B';
	else if(70<=score && score<=79)
		grade = 'C';
	else if(60<=score && score<=69)
		grade = 'D';
	else if(0<=score && score<=59)
		grade = 'E';
	return grade;
}


