#include <iostream>
using namespace std;

int main()
{
    
    int a, b;

    cout<<"Enter two numbers: "<<endl;
    cin>>a>>b;

    cout << "Before swapping." << endl;
    cout << "a = " << a << ", b = " << b << endl;

    a = a + b;
    b = a - b;
    a = a - b;

    cout << "\nAfter swapping." << endl;
    cout << "a = " << a << ", b = " << b << endl;

    return 0;
}