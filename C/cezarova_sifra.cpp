#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char** argv) {

// Cézarova šifra funguje tak že místo pùvodního písmena napíše písmeno o 1 vìtší pø. a=b
// retezec k zasifrovani
char s[100];
int posun; // o kolik se má posunout
int i;
printf("Zadejte o kolik se ma posunout\n");
scanf("%d",&posun);
printf("Zadejte vetu\n");
scanf("%s",s);
printf("Puvodni zprava: %s\n", s);
// hlavni cyklus
for (i = 0; s[i] != '\0'; i++) // 
{
    s[i] = s[i] + posun; // zpráva=zpráva+posun 
}

printf("Zasifrovana zprava: %s\n", s);

	return (EXIT_SUCCESS);
}
