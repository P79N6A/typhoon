#include <iostream>
using namespace std;

int main()
{
	int n;
	char one,two;
	cin>>n;
	while(n--)
	{
		cin>>one;
		cin>>two;
		if(one>two)
			cout<<one<<"<"<<two<<endl;
		else if(one<two)
			cout<<one<<">"<<two<<endl;
		else
			cout<<one<<"="<<two<<endl;
	}
} 