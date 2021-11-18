#include <iostream>
#include <cstdlib>
#include <stdlib.h>
#include <time.h>
using namespace std;

int main(int argc, char** argv)
{

int a;
int b;
//int c;
int vysledek1;
int vysledek0;
int ja;
int pokracovat;
int switch_;

do
{
srand (time(NULL));
a=rand() % 10;
b=rand() % 10;

cout<<a<<endl;
cout<<b<<endl;
cout<<"Scitani(1) odcitani(0)"<<endl;
vysledek1=a+b;
vysledek0=a-b;

cin>>switch_;
cout<<endl;
switch(switch_)
{
	case 1:
		cout<<"Napis vysledek(a+b)"<<endl;
		cin>>ja;
		if(ja==vysledek1)
			{
			cout<<"Spravne"<<endl;
			}
		else
			{
			cout<<"Neumis pocitat"<<endl;
			}
		break;
	
	case 0:
		{
		cout<<"Napis vysledek(a-b)"<<endl;
		cin>>ja;
		if(ja==vysledek0)
			{
			cout<<"Spravne"<<endl;
			}
		else
			{
			cout<<"Neumis pocitat"<<endl;
			}
		}
	break;	
}
cout<<"Chcete pokracovat(1/0)"<<endl;
cin>>pokracovat;
}
while(pokracovat==1);

cin.get();
cin.get();
return 0;
}

