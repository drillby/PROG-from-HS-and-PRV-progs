#include <iostream>
#include <algorithm>
using namespace std;

int main(void)
{

const int delkaPole = 6;
int pole[delkaPole] = { 1, 6, 9, 2, 6, 3 };
int c = count(pole, pole + delkaPole, 6);
cout <<"Cislo 6 se vyskytuje " << c << endl; // c = 2
cin.get();

return 0;
}
