#include<stdio.h>
#include<stack>
using namespace std;
typedef struct
{
	int row;
	int rank;
}Coordinate;
int main()
{
	Coordinate coordinate1;
	int row,rank;
	stack<Coordinate> stk;
	coordinate1 = { 1, 2};
	stk.push(coordinate1);
	coordinate1 = stk.top();
	row = coordinate1.row;
	rank = coordinate1.rank;
	stk.pop();
	printf("%d %d",row,rank);
	return 0;
}