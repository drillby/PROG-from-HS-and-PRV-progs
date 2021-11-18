#include <stdio.h>
#include <stdlib.h>

double faktorial(int n) // vytvoøení funkce faktorial
{
    if (n == 1)
        return 1;
    return n * faktorial(n - 1);
}
main() // samotný program
{
FILE * soubor1 = fopen("faktorial.txt", "r"); // ètení ze souboru	
FILE * soubor2 = fopen("faktorial_1.txt", "w");  // MUSÍ EXISTOVAT

if (soubor1 == NULL) // kontrola pro otevøení  
	{
	 printf("Soubor se nepodaøilo otevøít pro zápis, zkontrolujte prosím oprávnìní.");
	 return 1;
	}
	
char buffer[1024]; // buffer - daváme rádek ze souboru
fputs("TOTO JE KOPIE!", soubor2);
fputs("\n", soubor2);
while (fscanf(soubor1, " %1023[^\n]", buffer) != EOF)
    {
     printf("%s\n", buffer); // vypíšeme rádek z bufferu na obrazovku
	 fputs(buffer, soubor2);
     fputs("\n", soubor2);
    }

if (fclose(soubor1) == EOF) // zavøení souboru 
    {
     printf("Soubor se nepodaøilo uzavøít.");
     return 1;
    }
if (fclose(soubor2) == EOF) // zavøení souboru 
    {
     printf("Soubor se nepodaøilo uzavøít.");
     return 1;
    }

return (EXIT_SUCCESS);
}
