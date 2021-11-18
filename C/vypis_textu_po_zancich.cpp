#include <stdio.h>
#include <stdlib.h>

int main(int argc, char** argv) {

int i;
char veta[1501];
printf ("Zadejte vetu: \n");
scanf (" %1500[^\n]s", veta);
for (i = 0; veta[i] != '\0'; i++) //podminka funguje dokud znak ve vìtì je rùzný od 0, !=0
    printf("%c ", veta[i]); // %c jednotlivý znak, mezera za %c mezi každým zankem mezera 
	return (EXIT_SUCCESS);
}
