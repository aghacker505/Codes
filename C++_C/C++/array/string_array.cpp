#include <iostream>
#include <conio.h>

using namespace std;

int main()
{
    int n1, n2;
    char a[100];
    char b[100];
    int i;

    cout<<"Enter the size of fisrt name: ";
    cin>>n1;
    
    cout<<"Enter the size of second name: ";
    cin>>n2;
    
    for(i=0; i<n1; i++)
    {
        cout<<"Enter your first name character no."<<i+1<<": " ;
        cin>>a[i];
    }

    for(i=0; i<n2; i++)
    {
        cout<<"Enter your second name character no."<<i+1<<": " ;
        cin>>b[i];
    }

    cout<<"Your name is: \n";

    for(i=0; i<n1; i++)
    {
        cout<<a[i];
    }
    
    cout<<" "; 
    
    for(i=0; i<n2; i++)
    {
        cout<<b[i];
    }
    
    return 0;
    getch();
}