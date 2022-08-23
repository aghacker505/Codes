#include <stdio.h>
#include <conio.h>

void main()
{
    int n;
    int a[100];
    int i;
    int sum = 0, avg = 0;

    printf("Enter the size of array: ");
    scanf("%d" ,&n);
    
    for(i=0; i<n; i++)
    {
        printf("Enter element no.%d: " ,i+1 );
        scanf(" %d" , &a[i]);
    }

    printf("Elements of the array: \n");

    for(i=0; i<n; i++)
    {
        printf("%d \n" , a[i]);
    }
    
    for(i=0; i<n; i++)
    {
        sum = sum + a[i];
    }

    printf("The sum of the array elements are: %d\n", sum);
    avg = sum/n;
    printf("The average of the elements of the array is: %d" ,avg);


    getch();
}