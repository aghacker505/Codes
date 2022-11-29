#include <iostream>
using namespace std;

int main(){
    int a = 29, *ptr1, **ptr2;

    ptr1 = &a;
    ptr2 = &ptr1;

    cout<<"The address of 'a': "<<ptr1<<endl;
    cout<<"The address of a ptr1: "<<ptr2<<endl;
    cout<<**ptr2;
    cout<<endl;

    cout<<"after increment the address";
    ptr1 = ptr1 + 2;

    cout<<endl<<ptr1;

}