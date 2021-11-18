#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char** argv) {

int i;
int pom;
char veta[1501];
printf ("Zadejte vetu: \n");
scanf (" %1500[^\n]s", veta);
printf("%d znaku \n", strlen(veta));
pom=strlen(veta);
for (i = 0; pom-i+1 != 0 ; i++) //podminka funguje dokud znak ve vìtì je rùzný od 0, !=0, pom-i+1 je rùzný od 0
    printf("%c ", veta[pom-i]); // %c jednotlivý znak, mezera za %c mezi každým znakem mezera, pom-i jdeme od zadu 
	return (EXIT_SUCCESS);
}
