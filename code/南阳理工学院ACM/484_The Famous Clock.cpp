#include<iostream>
using namespace std;
int main()
{
	int n = 1;
	string s;
	while(cin >> s)
	{
		cout << "Case " << n++ << ": " ;
		switch(s[0])
		{
			case 'I' : if(s[1] != 'X' && s[1] != 'V')
							cout << s.size() << endl;
					   else if(s[1] == 'V')
							cout << 4 << endl;
					   else 
						    cout << 9 << endl; 
					   break;
			case 'V' : cout << 4 + s.size() << endl; break;
			case 'X' : cout << 9 + s.size() << endl; break;
		}
	}
}