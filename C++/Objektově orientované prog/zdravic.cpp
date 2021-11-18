#include <stdio.h>
#include <iostream>

using namespace std;

class Zdravic
{
public: 
		string text;
		int vek;
		string pozdrav(string jmeno);
		string hlaska(string co_reknu);
};

string Zdravic::pozdrav(string jmeno)
{
		return text + ", " + jmeno + "!\n";
}

string Zdravic::hlaska(string co_reknu)
{
		return "hlasim: " + co_reknu;
}

int main()
{
	Zdravic osoba;
	Zdravic zak;
	Zdravic ucitel;
	
	osoba.vek=45;
	zak.vek=16;
	ucitel.vek=50;
	
	zak.text= "ESKEREEE";
	osoba.text= "Zdravi osoba: Ahoj";
	ucitel.text= "Za 5!";
	
	cout<<osoba.pozdrav("Karle");
	cout<<"Je mi "<<osoba.vek<<" let."<<endl;
	cout<<osoba.pozdrav("Petre");
	
	
	cout<<zak.pozdrav("hoj");
	cout<<zak.pozdrav("Ahoj")<<zak.hlaska("vou pico nech me jet ")<<zak.vek<<endl;
	cout<<zak.text<<zak.hlaska("vou picoech me jet");	
	
	cin.get();
	return 0;
}
