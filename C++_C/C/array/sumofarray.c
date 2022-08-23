#include <stdio.h>
#include <conio.h>

void main()
{
    int a[5], i;
    int sum = 0;

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
        sum = sum + a[i];
    }

    printf("here is the sum of the elements you entered: %d" ,sum);

    getch();
}