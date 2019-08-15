#include<iostream>
#include<cstring>

using namespace std;

int KMP(string a,string b,int *next,int pos);
void get_next(string b, int *next);

int **next;//标记位置

static string *arr1 = new string[1000];//查询串
static string *arr2 = new string[1000];//查询串

int main()
{
	int num;
	cin>>num;
	next = new int*[num];
	//string *arr1 = new string[num];//查询串
	//string *arr2 = new string[num];//目标串
	for(int i=0;i<num;i++)
	{
		cin>>arr2[i];
		cin>>arr1[i];
		next[i] = new int[arr2[i].length()];
		memset(next[i],0,arr2[i].length()*sizeof(int));
	}
	int pos = 0;
	int n = 0;
	for(int i=0;i < num;i++)
	{
		while(arr1[i].length() - pos >= arr2[i].length())
		{
			pos = KMP(arr1[i],arr2[i],next[i],pos+1);
			if(pos == 0)
			{
				cout<<n<<endl;
				break;
			}
			else
			{
				n++;
			}
		}
		n = 0;
	}
	return 0;
}

//KMP字符串匹配算法
//pos:匹配位置
//return：返回匹配位置，没有匹配返回0
int KMP(string a,string b,int *next,int pos)
{
	//下标
	int a_sign = pos;  
    int b_sign = 0;
	bool isReset = false;
	get_next(b, next);
	while(a_sign < a.length() && b_sign < b.length())
	{
		if(isReset || a[a_sign] == b[b_sign])
		{
			++a_sign;
			if(isReset != true)
			{
				++b_sign;
			}
			else
			{
				isReset = false;
			}
		}
		else
		{
			if(b_sign!=0)
			{
				b_sign = next[b_sign]-1;
			}
			else
			{
				isReset = true;
			}
		}
	}
	if(b_sign == b.length())
	{
		return a_sign - b.length();
	}
	else
	{
		return 0;
	}
}

//标记元素重复的次数
void get_next(string b, int *next)
{
	int i,j;  
    i = 0;  
    j = 0;  
    next[0] = 0;  
    while(i < b.length())
	{  
        //b[i]表示后缀的单个字符  
        //b[j]表示前缀的单个字符  
        if( j==0 || b[i] == b[j-1])
		{  
            ++i;  
            ++j;  
            next[i] = j;  
        }
		else
		{  
            j = next[j-1];  
        }  
    }  
}