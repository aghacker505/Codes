#include <stdio.h>
#include <conio.h>

void main()
{
    float n, i;
    float sum;

    printf("Enter total number of terms to find the sum: ");
    scanf("%d", &n);

    for(i=1; i<=n; i++)
    {
        sum = sum + (1/i);
    }

    printf("sum is %d", sum);

    getch();
}