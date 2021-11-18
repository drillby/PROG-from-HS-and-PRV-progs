#include <iostream>
#include <algorithm>
using namespace std;

int main(void)
{

const int delkaPole = 5;
int pole[delkaPole] = { 2, 1, 4, 5, 3 };
int *i = max_element(pole, pole + delkaPole); //min_element- najde nejnizsi cislo
cout <<"Nejvetsi cislo je cislo " << *i <<endl ; // i = pole + 3, *i = 5, vypise co je nejvetsi cislo
cin.get();

return 0;
}
