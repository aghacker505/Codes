#include<iostream>
using namespace std;

void max(int a, int b, int c){
    cout<<"Enter first number: ";
    cin>>a;
    cout<<"Enter second number: ";
    cin>>b;
    cout<<"Enter third number: ";
    cin>>c;
    if (a>b){
        if (a>c){
            cout<<"Largest number is: "<<a;
        }
        else{
            cout<<"Largest number is: "<<c;
        }
    }

    else{
        if (b>c){
            cout<<"Largest number is: "<<b;
        }
        else{
            cout<<"Largest number is: "<<c;
        }
    }
}

int main(){
    int x,y,z;
    max(x,y,z);
    return 0;
}