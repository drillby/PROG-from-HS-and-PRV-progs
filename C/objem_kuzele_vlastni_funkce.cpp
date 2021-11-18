#include <stdio.h>
#include <stdlib.h>
#include <math.h>

float objem_kuzele (float a, float b) //a=polomer, b=vyska
{
    return(M_PI*a*a*b/3); //navratová hodnota
}

int main(int argc, char** argv) 
{
float v,r,p; // výška, polomìø, pøírustek
int poc; // poèet hodnot
r=0;

printf("Tabulka hodnot objemu kužele\n");
scanf("%f",&p);
printf("------------------\n");
printf("Zadejte vysku\n");
scanf("%f",&v); // pøírustek
printf("Zadejte pocet hodnot\n");
scanf("%f",&poc);
printf(".......................\n");
for(int i=0;i<poc;i++)
    {
r=r+p;
printf(" r= %6.2f   Objem kuzele = :%12.4f\n", r,objem_kuzele(r,v));
    }
return 0;
}
