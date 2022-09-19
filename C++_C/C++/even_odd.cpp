#include <iostream>
#include <conio.h>
using namespace std;

int main()
{
    int a;

    cout<<"Enter any number: ";
    cin>>a;

    if(a%2==0){
        cout<<"Given number is even";
    }

    else{
        cout<<"Given number is odd";
    }

    getch();
    return 0;
}