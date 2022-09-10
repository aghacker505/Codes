#include <iostream>
using namespace std;

int main(){
    int sub1, sub2, sub3, sub4, sub5;

    cout<<"Enter the marks of first subject: ";
    cin>>sub1;

    cout<<"Enter the marks of second subject: ";
    cin>>sub2;

    cout<<"Enter the marks of third subject: ";
    cin>>sub3;

    cout<<"Enter the marks of fourth subject: ";
    cin>>sub4;

    cout<<"Enter the marks of fifth subject: ";
    cin>>sub5;

    if((sub1+sub2+sub3+sub4+sub5)/5 <= 40){
        cout<<"You are fail";
    }

    else{
        cout<<"You are pass";
    }

    return 0;
}