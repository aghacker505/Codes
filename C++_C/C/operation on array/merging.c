// program to merge unsorted array

#include <stdio.h>
#include <conio.h>

int main()
{
    int i;
    int a[20], b[20], c[20], m, n;

    printf("Enter size of the array (a): ");
    scanf("%d", &m);

    printf("Enter Elements of an array (a): ");
    for(i=1;i<=m;i++)
    {
        scanf("%d", &a[i]);
    }

    printf("Elements of the array(a): ");
    for(i=1; i<=m;i++)
    {
        printf("%d\n", a[i]);
    }

    printf("Enter size of the array (b): ");
    scanf("%d", &n);

    printf("Enter Elements of an array (b): ");
    for(i=1;i<=n;i++)
    {
        scanf("%d", &b[i]);
    }

    printf("Elements of the array(b): ");
    for(i=1; i<=n;i++)
    {
        printf("%d\n", b[i]);
    }

    // merging of array

    int k = 1;
    for(i = 1; i <= m; i++)
    {
        c[k] = a[i];
        k++; 
    }
    
    for(i = 1; i<= n; i++)
    {
        c[k] = b[i];
        k++; 
    }

    printf("Merged array: \n");
    
    for (i = 1; i < k; i++)
    {
        printf("%d\n", c[i]); 
    }

    return 0;
}