#include <stdlib.h>
#include <stdio.h>
#include <conio.h>

struct node
{
    int info;
    struct node *link
};

void printlinklist(struct node *ptr){
    while(ptr != NULL){
        printf(" %d", ptr->info);
        ptr = ptr -> link;
    }
}

void main()
{
    struct node *start;
    struct node *one;
    struct node *two;
    struct node *three;
    // struct node *four;

    one = malloc(sizeof(struct node));
    two = malloc(sizeof(struct node));
    three = malloc(sizeof(struct node));

    one->info =29;
    two->info =01;
    three->info =12;
    // four->info = 69;

    one->link =two;
    two->link =three;
    // four->link =three;
    three->link =NULL;
    start = one;

    printlinklist(start);
    getch();
}