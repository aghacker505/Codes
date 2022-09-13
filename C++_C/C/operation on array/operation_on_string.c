#include <stdio.h>
#include <conio.h>
#include <string.h>

void main(){
    int l;
    char s1[20], s2[20], s3[20];

    printf("Enter any string: ");
    scanf("%s",s1);
    printf("Original string is: %s",s1);
    
    // copying string
    strcpy(s2,s1);
    printf("\nCopied string is: %s\n",s2);

    // reversing the string
    printf("After reversing the string: %s\n",strrev(s1));

    // addition of string
    strcat(s1,s2);
    printf("Addition of string: %s\n",s1);

    // length of the string
    l = strlen(s1);
    printf("Length of string is: %d\n",l);

    getch();
}