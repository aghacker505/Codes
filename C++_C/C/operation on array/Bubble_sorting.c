#include <stdio.h>
#include <conio.h>

void main()
{
    int a[100];
    int size;
    int i, j, temp;
    

    // creating array
    printf("Enter the size of your array: ");
    scanf("%d", &size);

    printf("Enter the elements of the array: ");
    for(i=0; i<size; i++)
    {
        scanf("\n%d", &a[i]);
    }

    printf("Original array: ");
        for(i=0; i<size; i++)
    {
        printf("%d ", a[i]);
    }

    // bubble sorting

    for(i=0; i<size-1; i++){
        for(j=0; j<size-i-1; j++){
            if (a[j]>a[j+1])
            {
                a[j] = temp;
                a[j] = a[j+1];
                a[j+1] = temp;
            }
        }
    }

    printf("\nSorted array: ");
        for(i=0; i<size; i++)
    {
        printf("%d ", a[i]);
    }
}