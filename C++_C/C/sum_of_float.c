#include <stdio.h>

int main()
{
    double x[2];
    int i;
    double sum = 0;

    for(i=0; i<2 ; i++)
    {
        printf("Enter value: \n");
        scanf("%lf" , &x[i]);
    }

    for (i=0; i<2 ; i++)
    {
        printf("Values tha you entered %lf \n" , x[i]);
    }

    for (i=0; i<2; i++)
    {
        sum = sum + x[i];
    }

    printf("sum of the number you enter:%lf  ", sum);
    return 0;
}

// '%lf' for doubles
// '%d' for integers
// '%f' for floats
// '%c' for single character 
// '%s' for strings 