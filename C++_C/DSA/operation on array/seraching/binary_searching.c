#include <stdio.h>
#include <conio.h>

void main()
{
    int n;
    int a[100];
    int i, mid, item;

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
    
    printf("\nEnter element to be search: ");
    scanf("%d", &item);
    
    int beg =0, end = n-1;
    mid = (beg+end)/2;

    while(beg<=end && a[mid] != item){
        if(a[mid]>item){
            end = mid-1;
        }
        else{
            beg = mid+1;
        }

        mid = (beg+end)/2;
    }

    if(a[mid] == item){
        printf("found at %d", mid);
    }
    else{
        printf("not found ");
    }
    getch();
}