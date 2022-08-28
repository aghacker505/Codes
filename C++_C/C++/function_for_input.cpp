#include <iostream>

using namespace std;

void display(int a)
{
    cout<<"Enter the number: "<<endl;
    cin>>a;
    cout<<"Here is the number you entered: "<<a<<endl;
}

int main()
{
    int x;
    display(x);
    return 0;
}