#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <cstdlib>

int main(int argc, char** argv) {

double a;
double b;
int volba;
double vysledek;
char pokracovat;
do // do-while pokaždé udìlá 1. cyklus a až pak se zeptá na podmínku 
{ 
std::system( "cls" ); //po vypoètení pøíkladu smaže cmd konzoli a kurkor nastavýdo výchozí polohy 
printf("Vitejte v kalkulacce \n");
printf("===================== \n");

printf("Zvolte si operaci: \n");

printf("1 - scitani \n");
printf("2 - odcitani \n");
printf("3 - nasobeni \n");
printf("4 - deleni \n");
printf("5 - mocnina na x\n");
scanf("%d", &volba);

if ((volba > 0) && (volba <= 5)) // podminka k switch, musi se upravit s kazdym pridanym case
    printf("Zadejte prvni cislo: \n"),scanf("%lf", &a),printf("Zadejte druhe cislo: \n"),scanf("%lf", &b); // if musí mít jen jeden øádek
    
else
    printf("Neplatna volba \n"); //když se zadá vìtší èíslo než je v if
    
switch(volba) //volba operace
{
    case 1:
        vysledek = a + b;
        break;
    case 2:
        vysledek = a - b;
        break;
    case 3:
        vysledek = a * b;
        break;
    case 4:
        vysledek = a / b;
        break;
    case 5:
    	vysledek = pow(a,b);
        break; 

}
printf("Vysledek: %f\n", vysledek);
printf("\n");
    printf("Prejete si zadat dalsi priklad? [1/0] \n"); //patøí k do-while 
    scanf("%d",  &pokracovat); // patøí k do-while

} while (pokracovat == 1); // prakticky jsme dali definici pokraèovat = 1 dali sem 
printf("Dekuji za pouziti kalkulacky");
	return (EXIT_SUCCESS);
}
