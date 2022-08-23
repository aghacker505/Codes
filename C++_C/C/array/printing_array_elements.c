#include <stdio.h>
#include <conio.h>

void main()
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