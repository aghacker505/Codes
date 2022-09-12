// Below is the program writen in C language but can also run in C++
// because C++ is the superset of C or we can also say that C is also applicable to C++ too.

#include <stdio.h>
#include <conio.h>

int main()
{
    int a[5],i;

    for (i=0; i<5; i++)
    {
        printf("Enter element of the an array: ");
        scanf("%d",&a[i]);
    }

    printf("Array elements are:- \n");

    for (i=0; i<5; i++)
    {
        printf("Element of array is: %d \n",a[i]);
    }

    getch();
}