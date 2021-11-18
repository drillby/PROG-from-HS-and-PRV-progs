#include <stdio.h>
#include <stdlib.h>

int main(int argc, char** argv) {
    FILE * p_soubor = fopen("neco.txt", "r"); // soubor musi bejt v defaultu èili na ploše
    FILE * p_soubor2 = fopen("kopie.txt", "w"); // musi existovat
if (p_soubor == NULL) // pro original
    {
     printf("Soubor se nepodaøilo otevøít pro ètení, zkontrolujte prosím zda existuje.");
     return 1;
    }
if (p_soubor2 == NULL) // pro kopii
    {
     printf("Soubor se nepodaøilo otevøít pro zápis, zkontrolujte prosím zda existuje.");
     return 1;
    }

char buffer[1024]; // buffer - daváme rádek ze souboru
fputs("TOTO JE KOPIE!", p_soubor2);
fputs("\n", p_soubor2);
while (fscanf(p_soubor, " %1023[^\n]", buffer) != EOF) // fscanf zapisuje do souboru p_soubor, ^ aby fscanf fungoval do entru ne do mezery, %1023 max.1023 znakù,
													  // != EOF konec souboru
    {
     printf("%s\n", buffer); // vypíšeme rádek z bufferu na obrazovku
	 fputs(buffer, p_soubor2);
     fputs("\n", p_soubor2);
    }

if (fclose(p_soubor) == EOF) // zavøení souboru 
    {
     printf("Soubor se nepodaøilo uzavøít.");
     return 1;
    }
if (fclose(p_soubor2) == EOF) // zavøení souboru 
    {
     printf("Soubor se nepodaøilo uzavøít.");
     return 1;
    }

return (EXIT_SUCCESS);
}
