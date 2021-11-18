#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char** argv)
{
    //pøeèteme èísla
    float cisla[5]; // pole
    printf("Zadejte serii 5 cisel:");
    scanf(" %f %f %f %f %f", cisla, cisla + 1, cisla + 2, cisla + 3, cisla + 4);

    //uloíme èísla do souboru
    FILE* soubor_k_zapisu = fopen("soubor.bin", "wb"); // soubor, wb zapis
    fwrite(cisla, sizeof (float), 5, soubor_k_zapisu); // adresa kde je pole ulozene, vypocita se velokost jednoho bloku(float), 5 casti z pole, pointer na soubor 
    fclose(soubor_k_zapisu);

    //vynulujeme pamì
    memset(cisla,0,sizeof(float)*5); // memset vynulovani pole, na cislo 0 pro 5 bloku float

    //pøeèteme èísla ze souboru
    FILE* soubor_ke_cteni = fopen("soubor.bin", "rb"); // rb cteni
    fread(cisla, sizeof (float), 5, soubor_ke_cteni); // pole, velikost float, soubor 
    fclose(soubor_ke_cteni);

    //vypíšeme èísla
    for (int i = 0; i < 5; i++)
        printf("Precteno: %f\n", cisla[i]);

    return (EXIT_SUCCESS);
}
