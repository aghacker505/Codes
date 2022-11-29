#include <iostream>
using namespace std;

class Base{
    public:
        void Print()
        {
            cout << "Base Class" << endl;
        }
};
class Derived : public Base{
    public:
        void Print()
        {
            cout << "Derived Class" << endl;
        }


};

int main()
{
    Base b1;
    Derived b2;
    b1.Print();
    b2.Print();
}