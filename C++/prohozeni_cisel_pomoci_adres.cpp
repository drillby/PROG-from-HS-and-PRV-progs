#include <stdio.h>
#include <stdlib.h>

void prohod(int *p_a, int *p_b)
{
    int pomocna = *p_a; // do pomocne kam ukazuje *p_a
    *p_a = *p_b; // kam ukazuje *p_a dame *p_b
    *p_b = pomocna; // kam ukazuje *p_b do promenne
}

////////////////////////////////////////////////////////////////

int main(int argc, char** argv) {
   
    int cislo1 = 15;
    int cislo2 = 8;
   
    printf("V A je cislo %d a v B je cislo %d.\n", cislo1, cislo2);
    prohod(&cislo1, &cislo2); // prikaz prohozeni
    printf("V A je cislo %d a v B je cislo %d.\n", cislo1, cislo2);
   
    return (EXIT_SUCCESS);
}
