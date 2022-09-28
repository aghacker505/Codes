#include <iostream>
using namespace std;

class Item{
    int number;
    float cost;

    public:
    void getdata(int a, float b);
    void putdata()
    {
        cout<<"The number is " << number<<endl;
        cout<<"The cost is " << number<<endl;
    }
};

void Item :: getdata(int a, float b)
{
    number = a;
    cost = b;
}

int main()
{
    Item I1, I2;
    I1.getdata(200, 20.3);
    I1.putdata();
    I2.getdata(400, 40.12);
    I2.putdata();

    return 0;
}