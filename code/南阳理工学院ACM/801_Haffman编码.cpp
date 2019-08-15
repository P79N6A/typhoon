#include<stdio.h>
#include <iostream>
#include <algorithm> 
#include <list>   
using namespace std;

typedef struct
{
	char chara;
	int weight;
}Note;

bool CompareRules(Note* _X, Note* _Y)
{
	if(_X->weight == _Y->weight)
		return _X->chara < _Y->chara;
	return _X->weight > _Y->weight;
}

int main()
{
	int n,i;
	list<Note> listOne;
	list<Note>::iterator i;   
	while(scanf("%d",&n)!=EOF)
	{
		while(n--)
		{
			Note note;
			scanf("%c %d",&note.chara,&note.weight);
			listOne.push_front(note);
		}
		while(listOne.size())
		{
			listOne.sort(CompareRules);
		}			
	}
	return 0;
}