#include <stdio.h>
#include <stdlib.h>

int main(int argc, char** argv) {

int j;
int i;
printf("Mala nasobilka pomoci dvou cyklu: \n");
for (j = 1; j <= 1000000; j++) //vnìjší for -  i=1.èíslo, i<=maximální èíslo kolik èísel se bude násobit, øádek 
{
    for (i = 1; i <= 1000000; i++) //vnitøní for - j=1.èíslo, j<=maximální èíslo co má kolikrát udìlat,sloupec
        printf("%4d ", i * j);
    printf("\n");
}
	return (EXIT_SUCCESS);
}
