#include <stdio.h>
#include <stdlib.h>

int main(int argc, char** argv) {


int pole[10]; // v[]je dolní index 
int i;
for (i = 0; i < 10; i++) 
{
    pole[i] = i +1;//sudé èíslo i * 2, liché èíslo i * 2 + 1
}

for (i = 0; i < 10; i++) //provede 10 cyklù sudé èíslo i * 2, liché èíslo i * 2 + 1
{
    printf("%d ", pole[i]); // vypíše èísla v indexu 1 až 10
}
	return (EXIT_SUCCESS);
}

