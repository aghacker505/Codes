#include <stdio.h>
#include <conio.h>

void main()
{
    int a[5], i;
    int pro = 1;

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
        pro = pro*a[i];
    }

    printf("Here is the product of all elements of array: %d" ,pro);

    getch();
}