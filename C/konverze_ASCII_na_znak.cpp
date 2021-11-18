#include <stdio.h>
#include <stdlib.h>

int main(int argc, char** argv) {

char c; // znak, který zadáme
int i; // ASCII hodnota znaku

c = 'a'; 
i = (int)c; // konverze znaku na ASCII
printf("Znak %c jsme pøevedli na ASCII hodnotu %d\n", c, i);

i = 98;
c = (char)i; // konverze ASCII na znak
printf("ASCII hodnotu %d jsme pøevedli na znak %c", c, i);
	return (EXIT_SUCCESS);
}
