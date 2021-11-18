#include <iostream>
#include <string>
#include <cmath>
#include <cstdlib>
using namespace std;

int main(int argc, char** argv) 
{
float a;
float b;
double vysledek;
int operace;


string pokracovat = "1";
while (pokracovat == "1")
{

cout<<"Vyberte poèetní operaci: "<<endl;

cout<<"1 - scitani"<<endl;
cout<<"2 - odcitani"<<endl;
cout<<"3 - nasobeni"<<endl;
cout<<"4 - deleni"<<endl;
cout<<"5 - sinus"<<endl;
cout<<"6 - cosinus"<<endl;
cout<<"7 - mocnina na x"<<endl;
cin>>operace;

cout<<"Vybrana operace:";
if(operace==1)
	cout<<"Scitani"<<endl;
	
else if(operace==2)
	cout<<"Odcitani"<<endl;

else if(operace==3)
	cout<<"Nasobeni"<<endl;

else if(operace==4)
	cout<<"Deleni"<<endl;

else if(operace==5)
	cout<<"Funkce sinus"<<endl;

else if(operace==6)
	cout<<"Funkce cosinus"<<endl;

else if(operace==7)
	cout<<"Mocnina na x"<<endl;
cout<<endl;
	
if(operace>=8)
	cout<<"Neplatna volba"<<endl;
	
if(operace<=4)
	{
	cout<<"Zadejte cislo a: "<<endl;
	cin>>a;
	cout<<"Zadejte cislo b: "<<endl;
	cin>>b;
	}

if((operace>=5) && (operace<=6))
	{
	cout<<"Zadejte uhel: "<<endl;
	cin>>a;	
	}
	
if(operace==7)
	{
	cout<<"Zadejte zaklad mocniny"<<endl;
	cin>>a;
	cout<<"Zadejte mocninu"<<endl;
	cin>>b;
	}

if(operace==1)
	vysledek=a+b;
	
else if(operace==2)
	vysledek=a-b;
	
else if(operace==3)
	vysledek=a*b;
	
else if(operace==4)
	vysledek=a/b;
	
else if(operace==5)
	vysledek = sin(a*M_PI/180.00);
	
else if(operace==6)
	vysledek = cos(a*M_PI/180.00);
	
else if(operace==7)
	vysledek = pow(a,b);
		
if(operace<=7)
	{
	cout<<"Vysledek je "<<vysledek<<endl;	
	cout<<endl;
	}
	
cout<<"Prejete si zadat dalsi priklad? [1/0]"<<endl;
cin>>pokracovat;
std::system( "cls" );
}

cin.get(); // ceka na stisk enteru
cin.get();
return 0;
}
