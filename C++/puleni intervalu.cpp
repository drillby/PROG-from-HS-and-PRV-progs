#include <iostream>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

int main()
{
	float a;
	float b;
	
	cout << "Zadejte vysku ze ktere bude micek hozen: ";
	cin >> a;
	cout << "Zadana vyska je(jsou) "<<a<<" metry(u)"<<endl;
	
	if(a<0,01)
	{
		b=a/2;	
		b=a;
		cout<<b<<endl;
	}
	else 
	{	
	cout <<"stiskni enter"<<endl;
	cin.get(); // ceka na stisk enteru
	cin.get();
	return 0;
	}
}
