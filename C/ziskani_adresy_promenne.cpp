#include <stdio.h>
#include <stdlib.h>

int main()
{
    int a, *p_a; // p_a volitený název, *potřeba, vytvoří se proměnná p_a a zapisujeme do ni adresu
    a = 56;
    printf("V pomenne a je %d\n", a);
    p_a = &a;                                                                  // uloží se adresa a do p_a
    printf("Ukazatel p_a ma hodnotu %p a ukazuje na hodnotu %d\n", p_a, *p_a); // %p=hexdec tvar
    *p_a = 15;                                                                 // uloží hodnotu 15 na adresu p_a
    printf("Ukazatel p_a ma hodnotu %p a ukazuje na hodnotu %d\n", p_a, *p_a);
    printf("V promenne a je %d\n", a);
    return (EXIT_SUCCESS);
}
