#include <stdio.h>
#include <stdlib.h>

int main(int argc, char** argv) {
    // Otevøení souboru pro pøipsání
    FILE * p_soubor = fopen("dopis.txt", "a"); // pro pøidání
    if (p_soubor == NULL)
    {
        printf("Soubor se nepodaøilo otevøít pro pøipsání, zkontrolujte prosím oprávnìní.");
        return 1;
    }

    // Zápis øádek do souboru
    fprintf(p_soubor, "\nPS: Vyžádej pomoc od Darma a Zanthie pro vybudování sil amuletu.\n"); // dopíše naposlední øádnek

    // Uzavøení souboru
    if (fclose(p_soubor) == EOF)
    {
        printf("Soubor se nepodaøilo uzavøít.");
        return 1;
    }

    return (EXIT_SUCCESS);
}
