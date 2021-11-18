#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

int main(int argc, char** argv) {

int maxInt = INT_MAX;
short maxShort = SHRT_MAX;
char maxChar = CHAR_MAX;
char sizeInt = sizeof(int);
char sizeShort = sizeof(short);
char sizeChar = sizeof(char);

printf("INT: zabírá %d bajt/y/ù a nejvìtší možné èíslo je %d\n", sizeInt, maxInt);
printf("SHORT: zabírá %d bajt/y/ù a nejvìtší možné èíslo je %d\n", sizeShort, maxShort);
printf("CHAR: zabírá %d bajt/y/ù a nejvìtší možné èíslo je %d\n", sizeChar, maxChar);

    return (EXIT_SUCCESS);
}

