#include <stdio.h>
#include <stdlib.h>

int main(int argc, char** argv) {

float a;
printf("Zadej cislo v rozmezi 10-20 nebo 30-40 \n");
scanf("%f", &a);
if (((a >= 10) && (a <= 20)) || ((a >=30) && (a <= 40))) // && a zároveò || nebo
    printf("Zadal jsi spravne \n");
    
else
    printf("Zadal jsi spatne \n");
	return (EXIT_SUCCESS);
}
