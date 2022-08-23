#include <stdio.h>
#include <conio.h>
#include <math.h>

void main()
{
    int a[5], i;
    int squ;

    printf("Enter the elements of the an array: ");

    for (i = 0; i < 5; i++)
    {
        scanf("%d", &a[i]);
    }

    printf("Array elements are: \n");

    for (i = 0; i < 5; i++)
    {
        printf("Element is: %d \n", a[i]);
    }

    for (i = 0; i < 5; i++)
    {
        squ = pow(a[i],2);
        printf("Here is the square of all elements of array: %d \n" ,squ);
    }

    getch();
}