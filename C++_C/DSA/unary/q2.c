#include <stdio.h>
#include <conio.h>

int main()
{
    int d;
    int a = 10;
    int b = 1;

    d = a++ + ++b;         // value of 'd' depends upon the value of 'b'
    // value of 'd' is change if we do increment in 'b' it is independent of incrementation in 'a'
    printf("%d %d %d", a, b, d);
    getch();
}