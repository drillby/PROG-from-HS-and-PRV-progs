#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(int argc, char** argv) {

float a;
float b;
printf("Vitejte v kalkulacce \n");
printf("Zadejte prvni cislo \n");
scanf("%f", &a);
printf("Zadejte druhe cislo \n");
scanf("%f", &b);
printf("Soucet: %4.3f \nRozdil: %4.3f \nSoucin: %4.3f \nPodil: %4.3f \nMocnina: %4.3f \nMocnina2: %4.3f \nOdmocnina: %4.3f \nOdmocnina2: %4.3f \nSinova_veta_soucet: %4.3f \nSinova_veta_rozdil: %4.3f \n", a+b, a-b, a*b, a/b, a*a, b*b, sqrt(a), sqrt(b), sin(a+b), sin(a-b));
printf("Cosinova_veta_soucet: %4.3f \nCosinova_veta_rozdil: %4.3f \n", cos(a+b), cos(a-b));
    return (EXIT_SUCCESS);
}

