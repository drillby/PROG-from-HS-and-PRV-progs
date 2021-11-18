#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char** argv)
{
char text [1024];
FILE * p_soubor = fopen("dopis1.txt", "a"); // musi byt vytvoren txt dopis1.txt

if (p_soubor == NULL)
	{
	 printf("Soubor se nepodaøilo otevøít pro zápis, zkontrolujte prosím oprávnìní.");
	}

printf("Zadejte text pro pridani: ");
scanf(" %1023[^\n]", text); // samotne zapsani max 1023 znaku

fputs(text, p_soubor);
fputs("\n",p_soubor);

if (fclose(p_soubor) == EOF) // zavøení souboru 
    {
     printf("Soubor se nepodaøilo uzavøít.");
     return 1;
    }

return (EXIT_SUCCESS);

}
