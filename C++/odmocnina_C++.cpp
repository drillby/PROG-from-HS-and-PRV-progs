#include <iostream>
#include <cmath>
using namespace std;

int main()
{

cout << "Zadej nejake cislo, ze ktereho spocitam odmocninu:" << endl;
int a;
cin >> a;
if (a >= 0)
{
    cout << "Zadal jsi nezaporne cislo, to znamena, ze ho mohu odmocnit!" << endl;
    double o = sqrt(double(a));
    cout << "Odmocnina z cisla " << a << " je " << o << endl;
}
else
    cout << "Odmocnina ze zaporneho cisla neexistuje!" << endl;
cout << "Dekuji za zadani" << endl;
cin.get(); cin.get();

return 0;
}
