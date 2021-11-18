#include <stdio.h>
#include <string>
#include <iostream>
#include <fstream>

using namespace std;

class BasketballTym
{
public: //public muzu upravovat kazdou slozku zvlast, privat musim zmenit vse najednou
	string jmeno;
	int zapasy;
	int vyhry;
	int prohry;
	
	void nastavitData(string jmenoSet, int zapasySet, int vyhrySet, int prohrySet) //vytvoreni atributu
		{
		jmeno=jmenoSet;
		zapasy=zapasySet;
		vyhry=vyhrySet;
		prohry=prohrySet;
		}
		
	void vypsaniTymu() //fce vypisujici atributy
		{
		cout<<"Jmeno: "<<jmeno<<endl;
		cout<<"Pocte zapasu: "<<zapasy<<endl;
		cout<<"Pocte vyher: "<<vyhry<<endl;
		cout<<"Pocte proher: "<<prohry<<endl;
		cout<<endl;
		}
};

int main()
{
BasketballTym lakers; //vytvoreni tridy
lakers.nastavitData("Los Angeles Lakers", 0, 0, 0); //nastaveni atributu
lakers.vypsaniTymu(); //zavolani fce co vypisuje

//zapsani do csv
ofstream ZapisDoSouboru("nba.csv");
ZapisDoSouboru<<"\n"<<lakers.jmeno<<";"<<lakers.zapasy+1<<";"<<lakers.vyhry+1<<";"<<lakers.prohry;
ZapisDoSouboru.close();

//vypsani z csv
string bunka;

ifstream CteniSouboru("nba.csv");
	
getline(CteniSouboru, bunka, ';');	
cout << bunka;
cout << " ";
	
getline(CteniSouboru, bunka, ';');
cout << bunka;
cout << " zapas, ";
	
getline(CteniSouboru, bunka, ';');
cout << bunka;
cout << " vyhra, ";
	
getline(CteniSouboru, bunka, ';');
cout << bunka;
cout << " prohra";



return 0;
}
