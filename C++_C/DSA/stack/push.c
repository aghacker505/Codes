#include <stdio.h>

void push()
{
    int value;
    if(s.top == MAXSIZE-1){
        print("Overflow");
        return;
    }

    s.top = s.top+1;
    printf("Enter the value to be insert");
    scanf("%d",&value);

    s.stack[s.top]=value;
    return;
}