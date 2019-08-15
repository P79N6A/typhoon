#include<iostream>

using namespace std;

bool IsBissextile(int year);
int RiQi(int *arr);

int main()
{
	int i,n;
	cin>>n;
	int **arr = new int*[n];
	for(i=0;i<n;i++)
	{
		arr[i] = new int[3];
		cin>>arr[i][0];
		cin>>arr[i][1];
		cin>>arr[i][2];
	}
	for(i=0;i<n;i++)
	{
		cout<<RiQi(arr[i])<<endl;
	}
	return 0;
}

int RiQi(int *arr)
{
	int i,sum=0;
	for(i=1;i<arr[1];i++)
	{
		switch(i)
		{
			case 1:sum += 31;break;
			case 2:if(IsBissextile(arr[0]))sum += 29;else sum += 28;break;
			case 3:sum += 31;break;
			case 4:sum += 30;break;
			case 5:sum += 31;break;
			case 6:sum += 30;break;
			case 7:sum += 31;break;
			case 8:sum += 31;break;
			case 9:sum += 30;break;
			case 10:sum += 31;break;
			case 11:sum += 30;break;
			case 12:sum += 31;break;
		}
	}
	sum += arr[2];
	return sum;
}

bool IsBissextile(int year)
{
	if((year % 400 == 0)||((year % 4 == 0)&&(year % 100 != 0)))
	{
		return true;
	}
	else
	{
		return false;
	}
}



