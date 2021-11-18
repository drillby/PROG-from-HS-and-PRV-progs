#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <cstdlib>

int main(int argc, char** argv) {

double a;
double b;
int volba;
double vysledek;
char pokracovat = 1;
printf("Vitejte v kalkulacce \n");
while (pokracovat == 1) //výbìr pokaèování 
{
std::system( "cls" ); //po vypoètení pøíkladu smaže cmd konzoli a kurkor nastavýdo výchozí polohy 
printf("Zadejte prvni cislo: \n");
scanf("%lf", &a);
printf("Zadejte druhe cislo: \n");
scanf("%lf", &b);
printf("Zvolte si operaci: \n");
printf("1 - scitani \n");
printf("2 - odcitani \n");
printf("3 - nasobeni \n");
printf("4 - deleni \n");
printf("5 - mocnina_a \n");
printf("6 - mocnina_b \n");
printf("7 - odmocnina_a \n");
printf("8 - odmocnina_b \n");
printf("9 - sin_a \n");
printf("10 - cos_a \n");
printf("11 - tan_a \n");
scanf("%d", &volba);
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
    	vysledek = a*a;
        break;
    case 6:
	    vysledek = b*b;
		break;   
	case 7:
	    vysledek = sqrt(a);
		break;
	case 8:
	    vysledek = sqrt(b);
		break;   
	case 9:
	    vysledek = sin(a*M_PI/180.00);
	case 10:
		vysledek = cos(a*M_PI/180.00);
	case 11:
		vysledek = tan(1*M_PI/180.00);
}
if ((volba > 0) && (volba <= 11)) // podminka k switch, musi se upravit s kazdym pridanym case
    printf("Vysledek: %f", vysledek);
else
    printf("Neplatna volba \n"); //když se zadá vìtší èíslo než je v if
printf("\n");
    printf("Prejete si zadat dalsi priklad? [1/0] \n"); //patøí k while 
    scanf("%d",  &pokracovat); // patøí k while

}
printf("Dekuji za pouziti kalkulacky");
	return (EXIT_SUCCESS);
}
