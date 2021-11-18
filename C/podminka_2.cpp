#include <stdio.h>
#include <stdlib.h>
#include <math.h> // Nesmíme zapomenout na include hlavièky math.h, obsahuje funkci pro odmocninu
int main(int argc, char** argv) {
    int a;
    printf("Zadej nejake cislo, ze ktereho spocitam odmocninu:  \n");
    scanf("%d", &a);
    if (a > 0)
    {
        printf("Zadal jsi cislo vetsi nez 0, to znamena, ze ho mohu odmocnit!\n");
        double o = sqrt(a);
        printf("Odmocnina z cisla %d je %.2f \n", a, o);
    }
    else
        printf("Odmocnina ze zaporneho cisla a 0 neexistuje \n");

    printf("Dekuji za zadani \n");
    return (EXIT_SUCCESS);
}
