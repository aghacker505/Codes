#include <stdio.h>
#include <conio.h>

void main() 
{
    int a[3][3];
    int row;
    int col;

    printf("Enter the elements of the matrix: ");

    for(row = 0; row <3; row++ )
    {                                                       //we can also write row at the place of col and col at the place of row
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

    getch();
}    