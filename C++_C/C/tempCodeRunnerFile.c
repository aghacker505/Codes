
        }
    }

    printf("Matrix is ");

    for(row = 0; row <3; row++ )
    {
        for (col = 0; col<3; col++)
        {
            printf( "%d ", a[row][col]);
        }
        printf("\n");
    }

    getch();
}