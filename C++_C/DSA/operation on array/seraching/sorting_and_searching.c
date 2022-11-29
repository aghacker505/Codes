#include <stdio.h>
#include <conio.h>

void main()
{
    int a[100];
    int size;
    int i, j, temp;
    int mid, item;
    

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
                temp = a[j];
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
    
    printf("\nEnter element to be search: ");
    scanf("%d", &item);
    
    int beg =0, end = size-1;
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