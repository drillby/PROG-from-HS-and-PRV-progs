#include <stdio.h>
#include <stdlib.h>

int main(int argc, char** argv)
{
    FILE* soubor;

if ((soubor = fopen("soubor.txt", "r"))== 0)
        printf("Soubor se nepodarilo otevrit pro cteni\n");
if ((soubor = fopen("soubor.txt", "w")) != 0)
        printf("Soubor se podarilo otevrit pro zapis\n");
if (fprintf(soubor, "It is Wendsday ma dude! ¡¡¡¡le Ëau") != 0)
        printf("Zapis do souboru se zdaril\n");
if (fclose(soubor) == 0)
        printf("Zavreni souboru se zdarilo\n");
if ((soubor = fopen("soubor.txt", "r")) != 0)
    {
        printf("Opetovny pokus o otevreni pro cteni se zdaril\n");
        fclose(soubor);
    }

if (rename("soubor.txt", "data.txt") == 0) // prejmenovani z x na y 
        printf("Prejmenovani souboru se zdrailo\n");
if ((soubor = fopen("soubor.txt", "r")) == 0) // overeni pro prejmenovani
        printf("soubor.txt se nepodarilo otevrit pro cteni\n");
if ((soubor = fopen("data.txt", "r")) != 0)
    {
        printf("data.txt se podarilo otevrit pro cteni\n");
        fclose(soubor);
    }
//if(remove("data.txt")==0)  smazani souboru
//        printf("Smazani data.txt se zdarilo\n");
//if ((soubor = fopen("soubor.txt", "r")) == 0)
//        printf("soubor.txt se nepodarilo otevrit pro cteni\n"); // kontrola
//if ((soubor = fopen("data.txt", "r")) == 0)
//        printf("data.txt se nepodarilo otevrit pro cteni\n"); // kontrola


    return (EXIT_SUCCESS);
}
