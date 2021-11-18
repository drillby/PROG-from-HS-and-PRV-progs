#include <stdio.h>
#include <stdlib.h>

int main(int argc, char** argv) {
    FILE * p_soubor = fopen("dopis.txt", "w"); // fopen název souboru, w=write/r=reade/a=apende
    if (p_soubor == NULL) // kontrolujem jestli soubor existuje/je místo na disku/máme práva k pøístupu
    {
        printf("Soubor se nepodaøilo otevøít pro zápis, zkontrolujte prosím oprávnìní.");
        return 1; // program konèí
    }

    fprintf(p_soubor, "Drahá Brynn,\n");
    fprintf(p_soubor, "opatruj se, Malcolm unikl a jistì si pro mne brzy pøijde jako pro prvního.\n");
    fprintf(p_soubor, "Musíš navést Brandona, dovést ho k amuletu, klíèem k zaøíkávadlu by možná\n");
    fprintf(p_soubor, "mohla být levandulová rùže.\n\n");
    fprintf(p_soubor, "Kallak\n");

    if (fclose(p_soubor) == EOF) // zavøení souboru
    {
        printf("Soubor se nepodaøilo uzavøít.");
        return 1;
    }

    return (EXIT_SUCCESS);
}
