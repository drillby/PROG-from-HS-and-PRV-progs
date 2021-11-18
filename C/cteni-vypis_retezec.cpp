#include <stdio.h>
#include <stdlib.h>

int main(int argc, char** argv) {

printf("Zadej své jméno: ");
char jmeno[51];
scanf("%50[^\n]s", jmeno); // ^ ukonèí výpis až po znáèknutí ENTER
printf("Ahoj uživateli %s, vítám tì!", jmeno);
	return (EXIT_SUCCESS);
}
