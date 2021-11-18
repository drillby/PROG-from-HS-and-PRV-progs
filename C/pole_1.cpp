#include <stdio.h>
#include <stdlib.h>
#define POCET 100 //všude kde pøekladaè najde POCET dosadí cislo !musí být velkými písmeny!

int main(int argc, char** argv) {
    // Vytvoøení pole
   long unsigned int soucet = 0; //aby se tam vešlo víc èísel
    int pole[POCET];
    int i, max, min;


for (i = 0; i < POCET; i++)
    {
        pole[i] = i * 2;  //sudé èíslo i * 2, liché èíslo i * 2 + 1
    }
min=pole[i];
max=pole[i];

    for (i = 0; i < POCET; i++)
    {
        printf("%5d ", pole[i]);
    }
    printf("\n");
for (i = 0; i<POCET; i++)
{
	if(pole[i]>max)
        max = pole[i]; //hledá maximum
    if(pole[i]<min)
        min=pole[i]; //hledá minimum
soucet = soucet +pole[i]; //souèet pole
}
printf("----------------------------------------------------------\n");
printf("Soucte prvku pole je %d, min je %d, max je %d, prumer hodnot je %d", soucet,min,max,soucet/POCET);
    return (EXIT_SUCCESS);
}
