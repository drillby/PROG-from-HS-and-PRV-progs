#include <stdio.h>
#include <stdlib.h>

void pozdrav(void) // void nemá žádnou návratovou hodnotu
{
    printf("Ahoj, vøele tì tu vítám!\n"); // vytvoøení funkce
}

int main(int argc, char** argv)
{

pozdrav(); // zavolání funkce

    return (EXIT_SUCCESS);
}
