#include <iostream>
#include <math.h>
using namespace std;

int main(int argc, char** argv)
{
	int min;
	int max;
	char rozhodnuti;
	int typ;
	
	cout<<"Zadejte minimalni hodnotu: ";
	cin>>min;
	cout<<"Zadejte maximalni hodnotu: ";
	cin>>max;
	while (rozhodnuti !='=')
	{
	typ=(max+min)/2;
	cout<<"Hadam: "<<typ<<endl;
	cout<<"Odpoved: ";
	cin>>rozhodnuti;
	if(rozhodnuti =='+')
		{
		min=typ+1;
		}
	if(rozhodnuti =='-')
		{
		max=typ-1;
		}
	if(rozhodnuti =='=')
		{
		cout<<"Kouzelne cislo je: "<<typ;
		}	
	
	}
	
	cin.get(); // ceka na stisk enteru
	cin.get();
	return 0;
}

