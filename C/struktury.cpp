#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct // definice nového typu, jedná se o strukturu, jedná se o promìnnou
{
    char jmeno[51]; // pole, rozsah 51
    int vek; // int 
    char ulice[51]; // pole, rozsah 51
    int psc;
    char mesto[51];  
    int mobil;
    char emial[51]; 
} ZACI;// název promìnný(mùže i malá písmena)

int main(int argc, char** argv) // vlastní program
{
	ZACI uzivatele[10]; //  

	//vytvoøení uživatele 0
    strcpy(uzivatele[0].jmeno, "subjekt1"); // strcpy - kopíruje øetìzec "Tomáš Marný" do øetìzce uzivatele[0].jmeno
    uzivatele[0].vek = 33; 
    strcpy(uzivatele[0].ulice, "ulice1");
    uzivatele[0].psc = 27401;
    strcpy(uzivatele[0].mesto, "mesto1");
    uzivatele[0].mobil = 123456789;
    strcpy(uzivatele[0].emial, "email1");

	//vytvoøení uživatele 1
    strcpy(uzivatele[1].jmeno, "subjekt2"); // strcpy - kopíruje øetìzec "Tomáš Marný" do øetìzce uzivatele[0].jmeno
    uzivatele[1].vek = 33; 
    strcpy(uzivatele[1].ulice, "ulice2");
    uzivatele[1].psc = 27401;
    strcpy(uzivatele[1].mesto, "mesto2");
    uzivatele[1].mobil = 123456789;
    strcpy(uzivatele[1].emial, "email2");
    
     strcpy(uzivatele[2].jmeno, "subjekt3"); // strcpy - kopíruje øetìzec "Tomáš Marný" do øetìzce uzivatele[0].jmeno
    uzivatele[2].vek = 33; 
    strcpy(uzivatele[2].ulice, "ulice3");
    uzivatele[2].psc = 27401;
    strcpy(uzivatele[2].mesto, "mesto3");
    uzivatele[1].mobil = 123456789;
    strcpy(uzivatele[1].emial, "email3");
    
     strcpy(uzivatele[3].jmeno, "subjekt4"); // strcpy - kopíruje øetìzec "Tomáš Marný" do øetìzce uzivatele[0].jmeno
    uzivatele[3].vek = 33; 
    strcpy(uzivatele[3].ulice, "ulice4");
    uzivatele[3].psc = 27401;
    strcpy(uzivatele[3].mesto, "mesto4");
    uzivatele[3].mobil = 123456789;
    strcpy(uzivatele[3].emial, "email4");

    int i; // definice 
    for (i = 0; i < 4; i++) // cyklus který vypíše všechny uživatele	
    {
    	printf("________________________\n");
        printf("Uživatel na indexu %d\n", i);
        printf("Jméno: %s\n", uzivatele[i].jmeno);
        printf("Vìk: %d\n", uzivatele[i].vek);
        printf("Ulice: %s\n\n", uzivatele[i].ulice);
        printf("psc: %d\n\n", uzivatele[i].psc);
        printf("mesto: %s\n\n", uzivatele[i].mesto);
        printf("mobil: %d\n\n", uzivatele[i].mobil);
        printf("emial: %s\n\n", uzivatele[i].emial);
    }
    return (EXIT_SUCCESS);
}
