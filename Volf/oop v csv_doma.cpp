#include <stdio.h>
#include <string>
#include <iostream>
#include <fstream>
#include <cstdlib>
#include <stdlib.h>

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
		
//	void vypsaniDatTymu()
};

int main()
{
//vypsani z csv
string nazevCSV, zapasCSV, vyhraCSV, prohraCSV, bunka, nazevCSV2, zapasCSV2, vyhraCSV2, prohraCSV2;

ifstream CteniSouboru("nba.csv");

cout<<"Vypsani z CSV"<<endl;

getline(CteniSouboru, bunka, '\n');

getline(CteniSouboru, nazevCSV, ';');	
cout << nazevCSV;
cout << " ";
	
getline(CteniSouboru, zapasCSV, ';');
cout << zapasCSV;
cout << " zapasu, ";
	
getline(CteniSouboru, vyhraCSV, ';');
cout << vyhraCSV;
cout << " vyher, ";
	
getline(CteniSouboru, prohraCSV, ';');
cout << prohraCSV;
cout << " proher"<<endl;

cout<<"Konec vypsani z CSV"<<endl<<endl;


std::string zapas = zapasCSV;
int nastavitzapas = std::atoi(zapas.c_str());

std::string vyhry = vyhraCSV;
int nastavitvyhry = std::atoi(vyhry.c_str());

std::string prohry = prohraCSV;
int nastavitprohry = std::atoi(prohry.c_str());


BasketballTym lakers; //vytvoreni tridy
lakers.nastavitData("Los Angeles Lakers", nastavitzapas, nastavitvyhry, nastavitprohry); //nastaveni atributu
lakers.vypsaniTymu(); //zavolani fce co vypisuje


BasketballTym nuggets;
nuggets.nastavitData("Denver Nuggets", nastavitzapas, nastavitvyhry, nastavitprohry);
nuggets.vypsaniTymu();



//zapsani do csv
int volba;
cout<<"Lakers vyhra, nebo prohra?"<<endl;
cout<<"1-vyhra"<<endl;
cout<<"2-prohra"<<endl;
cin>>volba;

if(volba==1)
	{
	
	ofstream ZapisDoSouboru("nba.csv");
	ZapisDoSouboru<<"Nazev"<<";"<<"poc. zapasu"<<";"<<"poc.vyher"<<";"<<"poc. proher"<<"\n";
	ZapisDoSouboru<<lakers.jmeno<<";"<<lakers.zapasy+1<<";"<<lakers.vyhry+1<<";"<<lakers.prohry;
	ZapisDoSouboru.close();
	}
	
else if(volba==2)
	{
	ofstream ZapisDoSouboru("nba.csv");
	ZapisDoSouboru<<"Nazev"<<";"<<"poc. zapasu"<<";"<<"poc.vyher"<<";"<<"poc. proher"<<"\n";
	ZapisDoSouboru<<lakers.jmeno<<";"<<lakers.zapasy+1<<";"<<lakers.vyhry<<";"<<lakers.prohry+1;
	ZapisDoSouboru.close();
	}

return 0;
}
