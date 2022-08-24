#include <stdio.h>
#include <conio.h>

int main()
{
    int d;
    int a = 1;
    int b = 2;

    d = a++ + ++b;
    printf("%d %d %d", d, a, b);
    getch();
}