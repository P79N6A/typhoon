#include<iostream>
#include<string>
using namespace std;
int main()
{
	string ori;
	string fnd = "you";
	string rep = "we";
	while(getline(cin, ori))
	{
		while(ori.find(fnd)!=string::npos)
			ori = ori.replace(ori.find(fnd), fnd.length(), rep); 
		cout<<ori<<endl;
	}
	return 0;
}