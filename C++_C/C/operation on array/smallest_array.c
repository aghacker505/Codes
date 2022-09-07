#include<stdio.h>
#include<conio.h>
#define MAX 10

void main()
{
    int a[MAX];
    int n,i;
    int min,item;

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

    min = a[1];
    for(i=2;i<=n;i++)
    {
        if (min>a[i]){
            min = a[i];
        }
    }

    printf("Smallest element of the array is: %d", min);
    getch();
}