#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;
//////////////////////////////// vytvoreni kostky+definice co ma delat 
class Kostka
{
public:
	Kostka(); //konstrutor,musí mít stejný název jako class
	~Kostka(); //destruktor, na konci protgramu se objekty znièí
    int pocet_sten;
    int hod(); //prototyp metody
};

Kostka::Kostka() // stejne jako class
{
	pocet_sten=6;
	cout<<"Volani bezparametrickeho konstruktoru"<<endl;
}

Kostka::~Kostka()
{
	cout<<"Zniceni kostek"<<endl;
}

int Kostka::hod() // metoda hod()
{
	return rand() % pocet_sten+1; //samotny hod, % zbytek po celociselnem deleni 
}
////////////////////////////////////////////////
int main()
{
	srand(time(NULL)); // bere cas pocitace, zvysuje nahodnmost hodu
	Kostka k,sestisten,mince; // vola se konstruktor, vsechno ma 6 sten 
	mince.pocet_sten=2; // prepsani na 2 steny
	
		cout<<"Hody s kostkou k "<<k.pocet_sten<<" sten"<<endl;
		for (int j=0; j<50; j++) //50x hodime kostku
			cout<<k.hod()<<" ";
		cout<<endl; cout<<endl;
//////////////////////////////////////
		cout<<"Hody s sestistenem "<<sestisten.pocet_sten<<" sten"<<endl;
		for (int j=0; j<50; j++) //50x hodime kostku
			cout<<sestisten.hod()<<" ";
		cout<<endl; cout<<endl;
/////////////////////////////////////		
		cout<<"Hody s minci "<<mince.pocet_sten<<" steny"<<endl;
		for (int j=0; j<10; j++) //50x hodime kostku
			if (mince.hod()==1)
			{
			cout<<"Panna ";	
			}
			else
			{
			cout<<"Orel ";
			}
			cout<<mince.hod()<<" ";
		cout<<endl; cout<<endl;

	
}
