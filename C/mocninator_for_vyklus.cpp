#include <stdio.h>
#include <stdlib.h>

int main(int argc, char** argv) {

int i;
float a;
int n;
double vysledek;
printf("Mocninator \n");
printf("========== \n");
printf("Zadejte zaklad mocniny: \n");
scanf("%f", &a); //mùže i záporné èíslo
printf("Zadejte exponent: \n");
scanf("%d", &n);

vysledek = a;
if (n==0)
    printf("Vysledek: %lf \n", vysledek=1); //a na nultou =1
else
    {
     for (i = 1; i <= (n - 1); i++)
      vysledek = vysledek * a;
	  printf("Vysledek: %lf\n", vysledek);
	  }



printf("Dekuji za pouziti mocninatoru \n");
	return (EXIT_SUCCESS);
}
