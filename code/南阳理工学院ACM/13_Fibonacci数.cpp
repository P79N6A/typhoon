#include "iostream"  
using namespace std;  
  
int Fibonacci(int n);

int main()  
{  
	int num,i; 
	cin>>num;
	int *arr = new int[num];
	for(i=0;i<num;i++)
	{
		cin>>arr[i];
	}
	for(i=0;i<num;i++)
	{
		cout<<Fibonacci(arr[i])<<endl;
	}
    return 0;  
}  

int Fibonacci(int n)
{
	if(n==1||n==2)
	{
		return 1;
	}
	else
	{
		return Fibonacci(n-1) + Fibonacci(n-2);
	}
}