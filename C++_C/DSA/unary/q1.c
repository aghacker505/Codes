#include <stdio.h>
#include <conio.h>

int main()
{
    int d;
    int a = 10;
    int b = 1;

    d = a++ + ++b;
    // d = a++ +++b;  this is wrong 
    printf("%d %d %d", a, b, d);
    getch();
}