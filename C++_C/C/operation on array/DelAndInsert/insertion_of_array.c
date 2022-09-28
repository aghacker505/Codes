#include <stdio.h>
#include <conio.h>
#define MAX 10

void main()
{
    int a[MAX];
    int i;
    int pos, item, n, size,j;

    printf("Enter the size of the array: ");
    scanf("%d", &n);

    for(i=1; i<=n; i++)
    {
        printf("Enter elements of the array: ");
        scanf("%d", &a[i]);
    }

    printf("Enter position to insert element: ");
    scanf("%d", &pos);

    printf("Enter the element to be entered: ");
    scanf("%d", &item);
    j=n;

    while (j>=pos)
    {
        a[j+1] = a[j];
        j = j-1;
    }

    a[pos] = item;
    n= n+1;

    printf("updated array: ");
    for (i=1; i<=n; i++)
    {
        printf("%d ", a[i]);
    }

    getch();
}