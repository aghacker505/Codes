#include <iostream>
#include <conio.h>
using namespace std;

class person
{
    char name[30];
    int age;

    public:
        void getdata(void);
        void display(void);
};

void person :: getdata(void)
{
    cout<<"Enter your name: ";
    cin>>name;
    cout<<"Enter your age: ";
    cin>>age;
}

void person :: display(void)
{
    cout<<"Name is: "<<name;
    cout<<"\nAge is: "<<age;
}

int main()
{
    person p;

    p.getdata();
    p.display();

    getch();
    return 0;
}