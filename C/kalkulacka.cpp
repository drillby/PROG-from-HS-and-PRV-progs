#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(int argc, char** argv) {

float a;
float b;
float soucet; 
float rozdil;
float socin;
float podil;
float mocnina;
float mocnina2;
float odmocnina;
float odmocnina2;

soucet = a + b;
rozdil = a - b;
soucet = a * b;
podil = a / b;
mocnina = a * a;
mocnina2 = b * b;
odmocnina = sqrt(a);
odmocnina2 = sqrt(b);

printf("Zadejte prvni cislo: ");
scanf("%f", &a);
printf("Zadejte druhe cislo: ");
scanf("%f", &b);

    return(EXIT_SUCCESS);
}
