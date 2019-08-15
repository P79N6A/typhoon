#include<iostream>
using namespace std;

int main()
{
    int n;
    cin>>n;
    int *arr=new int[n];
    for(int i=0;i<n;i++)
    {
        cin>>arr[i];
    }
    for(int i=0;i<n;i++)
    {
        for(int j=1;j<=arr[i];j++)
        {
            if(j%2==1)
            {
                cout<<j<<" ";
            }
        }
        cout<<endl;
        for(int j=1;j<=arr[i];j++)
        {
            if(j%2==0)
            {
                cout<<j<<" ";
            }
        }
        cout<<endl<<endl;
    }
    delete[] arr;
    return 0;
}