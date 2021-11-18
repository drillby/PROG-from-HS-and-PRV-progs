#include <stdio.h>
#include <stdlib.h>

int main(int argc, char** argv) {

float a;
char c;
printf("Zadej cislo mimo rozmezi 10-20 nebo 30-40 \n");
scanf("%f", &a);
if (!(((a >= 10) && (a <= 20)) || ((a >=30) && (a <= 40)))) // && a zároveò || nebo ! negace musí být v () - je to podmínka
    printf("Zadal jsi spravne \nA co takhle?\n");
else
    printf("Zadal jsi spatne \n");	
    return (EXIT_SUCCESS);

c=getchar();
c=getchar();
}
