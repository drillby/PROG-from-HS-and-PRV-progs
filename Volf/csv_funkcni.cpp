#include <iostream>
#include <fstream>
using namespace std;

int main(int agrc, char** agrv) {
	string a = "prvni text";
	ofstream ZapisDoSouboru("soubor.csv");
	ZapisDoSouboru << a <<";"<< a << ";" << a << ";" << a;
	ZapisDoSouboru.close();
	
	string bunka;
	
	
	ifstream CteniSouboru("Klub.csv");
	
	getline(CteniSouboru, bunka, ';');
	
	cout << bunka;
	cout << " ";
	
	return 0;
}
