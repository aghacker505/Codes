#include <iostream>
#include <conio.h>

using namespace std;

int main()
{
    int n;
    int a[100];
    int i;

    cout<<"Enter the size of array: ";
    cin>>n;
    
    for(i=0; i<n; i++)
    {
        cout<<"Enter element no."<<i+1<<": " ;
        cin>>a[i];
    }

    cout<<"Elements of the array: \n";

    for(i=0; i<n; i++)
    {
        cout<<a[i]<<endl;
    }
    
    return 0;
    getch();
}