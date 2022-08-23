#include <stdio.h>
#include <conio.h>

void main()
{
    int a[3][3];
    int row;
    int col;
    int sum = 0;

    printf("Enter the elements of the matrix: ");

    for(row = 0; row <3; row++ )
    {
        for (col = 0; col<3; col++)
        {
            scanf("%d", &a[row][col]);
        }
    }

    printf("Matrix is \n");

    for(row = 0; row <3; row++ )
    {
        for (col = 0; col<3; col++)
        {
            printf( "%d ", a[row][col]);
        }
        printf("\n");
    }

    for(row = 0; row <3; row++ )
    {
        for (col = 0; col<3; col++)
        {
            sum = sum + a[row][col];          
        }
    }

    printf("sum of matrix elements = %d", sum);

    getch();
}