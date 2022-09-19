#include<stdio.h>
#include<conio.h>
#define MAX 10

void main()
{
    int a[MAX];
    int n,i;
    int pos,item;

    printf("Enter size of the array: ");
    scanf("%d", &n);

    printf("Enter elements of the array: ");
    for(i=1;i<=n;i++)
    {
        scanf("%d", &a[i]);
    }
    
    printf("Elements of the array: \n");
    for(i=1;i<=n;i++)
    {
        printf("%d\n", a[i]);
    }

    printf("Enter the deletion positon: ");
    scanf("%d", &pos);
    
    item = a[pos];
    while (pos<n)
    {
        a[pos] = a[pos+1];
        pos = pos+1;
    }
    n = n-1;
    printf("Updated array: \n");
    for(i=1;i<=n;i++)
    {
        printf("%d\n", a[i]);
    }

    getch();
}