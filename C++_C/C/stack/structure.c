#include <stdio.h>
#include <conio.h>
#define MAXSIZE 5

struct stk{
    int stack[MAXSIZE];
    int top;
}s;

void push();
int pop();
void display();

void main(){
    int choice = 1;
    int option;
    s.top=-1;
    printf("1. Push opreation");
    printf("2. Pop opreation");
    printf("3. Display");
    printf("Enter option =");
    scanf(" %d", &option);

    switch (option)
    {
    case 1:
        break;
    
    default:
        break;
    }
}