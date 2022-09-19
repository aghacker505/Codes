#include <iostream>
#include <string>
#include <conio.h>

using namespace std;

void display(string name)
{
    cout<<"Enter your name: "<<endl;
    cin>>name;
    cout<<"your name is: "<<name<<endl;
}

int main()
{
    display("");
    getch();
    return 0;
}
