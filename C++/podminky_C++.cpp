#include <iostream>
#include <string>

using namespace std;

int main(void) {

cout << "Zadej nejake cislo" << endl;
int a;
cin >> a;
if (a > 5)
     cout << "Zadal jsi cislo vetsi nez 5!" << endl;
else cout << "Zadal jsi cislo mensi nez 5!" << endl;
cout << "Dekuji za zadani" << endl;
cin.get(); cin.get();
	return 0;
}
