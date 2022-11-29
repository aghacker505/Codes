// this program is to find the sum of square of n natural numbers
// 1^2 + 2^2 + 3^2 .......... + n^2

#include <stdio.h>
#include <conio.h>

void main()
{
    int n, i;
    int sum;

    printf("Enter total number of terms to find the sum: ");
    scanf("%d", &n);

    for(i=1; i<=n; i++)
    {
        sum = sum + (i*i);
    }

    printf("sum is %d", sum);

    getch();
}