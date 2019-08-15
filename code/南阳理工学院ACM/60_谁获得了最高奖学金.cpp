#include<iostream>
using namespace std;

int main()
{
	int n,manNum,SumMoney,nowMoney,nowSign,manMoney;
	int endGrade,classGrade,paperNum;
	char isCadre,isWest;
	cin>>n;
	string arr,nowName;
	while(n--)
	{
		SumMoney = 0;
		nowSign = 0;
		manMoney = 0;
		nowName = "";
		cin>>manNum;
		
		while(manNum--)
		{
			nowMoney = 0;
			
			cin>>arr;
			cin>>endGrade;
			cin>>classGrade;
			cin>>isCadre;
			cin>>isWest;
			cin>>paperNum;
			
			if(endGrade>80 && paperNum>0) nowMoney += 8000;
			if(endGrade>85 && classGrade>80) nowMoney += 4000;
			if(endGrade>90) nowMoney += 2000;
			if(endGrade>85 && isWest=='Y') nowMoney += 1000;
			if(classGrade>80 && isCadre=='Y') nowMoney += 850;
			
			if(nowMoney > manMoney)
			{
				nowName = arr;
				manMoney = nowMoney;
			}
			SumMoney += nowMoney;
		}	
		cout<<nowName<<endl;
		cout<<manMoney<<endl;
		cout<<SumMoney<<endl;
	}
	return 0;
}