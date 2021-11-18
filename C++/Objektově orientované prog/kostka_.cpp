#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

class Kostka
{
public:
	Kostka(int kolik_sten); //konstrutor s parametrem
	~Kostka(); //destruktor, na konci protgramu se objekty znièí
    int jaka_kostka; // atribut
    int hod(); //prototyp metody
};

Kostka::Kostka(int kolik_sten) // stejne jako class, volani kontruktoru s parametrem
{
	jaka_kostka=kolik_sten;
	srand(time(NULL));
}

Kostka::~Kostka()
{
	cout<<"Zniceni kostek"<<endl;
}

int Kostka::hod() // metoda hod()
{
	return rand() % jaka_kostka+1; //samotny hod, % zbytek po celociselnem deleni 
}

//tvorba globalni instance, vytvoreni objektu pred main, plati pro cely program 
Kostka kostka_4(2), kostka_2(9), kostka_1(6); // v zavorce je pocet sten

int main()
{
	Kostka kostka_3(4); // lokalni vytvoreni
	cout<<endl;
	cout<<"1. hod s 10 kostkami "<<kostka_1.jaka_kostka<<" sten"<<endl;
	for (int j=0; j<10; j++) //10x hodime kostku
		cout<<kostka_1.hod()<<" ";
		cout<<endl;
	cout<<"Stiskni klavesu"<<endl;
	cin.get(); //pocka
///////////////
		cout<<"2. hod s 10 kostkami "<<kostka_2.jaka_kostka<<" sten"<<endl;
	for (int j=0; j<10; j++) //10x hodime kostku
		cout<<kostka_2.hod()<<" ";
		cout<<endl;
	cout<<"Stiskni klavesu"<<endl;
	cin.get(); //pocka
///////////////	
		cout<<"3. hod s 10 kostkami "<<kostka_3.jaka_kostka<<" sten"<<endl;
	for (int j=0; j<10; j++) //10x hodime kostku
		cout<<kostka_3.hod()<<" ";
		cout<<endl;
	cout<<"Stiskni klavesu"<<endl;
	cin.get(); //pocka
///////////////	
		cout<<"4. hod s 10 mincemi "<<kostka_4.jaka_kostka<<" sten"<<endl;
	for (int j=0; j<10; j++) //10x hodime kostku
		cout<<kostka_4.hod()<<" ";
		cout<<endl;
	cout<<"Stiskni klavesu"<<endl;
	cin.get(); //pocka
return 0;

}
