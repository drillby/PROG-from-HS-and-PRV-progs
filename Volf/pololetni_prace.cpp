#include <iostream>
#include <string>
#include <cmath>
#include <cstdlib>
#include <cstdio>
#include <fstream>
using namespace std;

int main(int argc, char** argv) 
{
float a;
float b;
double vysledek;
int operace;
ofstream myfile;


cout<<"Vyberte poèetní operaci: "<<endl;

cout<<"1 - scitani"<<endl;
cout<<"2 - odcitani"<<endl;
cout<<"3 - nasobeni"<<endl;
cout<<"4 - deleni"<<endl;

cin>>operace;

cout<<"Vybrana operace: ";
if(operace==1)
	cout<<"Scitani"<<endl;
	
else if(operace==2)
	cout<<"Odcitani"<<endl;

else if(operace==3)
	cout<<"Nasobeni"<<endl;

else if(operace==4)
	cout<<"Deleni"<<endl;
	
if(operace<=4)
	{
	cout<<"Zadejte cislo a: "<<endl;
	cin>>a;
	cout<<"Zadejte cislo b: "<<endl;
	cin>>b;
	}

else
	{
	cout<<"Zadejte platnou pocetni operaci!"<<endl;
	cin.get();
	return 0;
	}

if(operace==1)
	vysledek=a+b;
	 
else if(operace==2)
	vysledek=a-b;
	
else if(operace==3)
	vysledek=a*b;
	
else if(operace==4)
	vysledek=a/b;
	
cout<<"Vysledek je "<<vysledek<<endl;
cout<<"Podivej se do textaku kalkulacka.txt"<<endl;

myfile.open("kalkulacka.txt");

if (myfile.is_open())
	{
    myfile<<"Priklad ktery jsi zadal je:"<<endl;
    myfile<<a;
    if (operace==1)
    	myfile<<"+";
    	
    else if (operace==2)
    	myfile<<"-";
    	
    else if (operace==3)
    	myfile<<"*";
    	
    else if (operace==4)
    	myfile<<"/";
    	
	myfile<<b;
	myfile<<"=";
	myfile<<vysledek;
    myfile.close();
	}

else 
cout<<"Nelze otevrit notepad";


cin.get(); // ceka na stisk enteru
cin.get();
return 0;
}
