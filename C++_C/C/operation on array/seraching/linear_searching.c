#include <stdio.h>
#include <conio.h>
#define MAX 100 

void main(){
    int size, item, i;
    int arr[MAX];

    printf("Enter the size of the array: ");
    scanf("%d", &size);
    
    printf("Enter the items of the array: ");
    for(i=0; i<size; i++)
    {
        scanf("%d", &arr[i]);
    }

    printf("Elements in the array: ");
    for(i=0; i<size; i++)
    {
        printf("\n%d", arr[i]);
    }

    printf("\nEnter element to be search: ");
    scanf("%d", &item);
    arr[size] = item;

    for(int i = 0; i < size+1; i++)
    {
        if (arr[i] == item){
            break;
        }
    }

    if(i == size)
    {
        printf("Not found");
    }

    else{
        printf("Found %d", i);
    }

    getch();
}
