#include <iostream>
#include <string>
#include <cmath>
using namespace std;
float a;
float b;
float c;
float d;
float dis;
float x1;
float x2;
int main() 
{
	cout << "bod a: "; //vypise bod a:
	cin >> a;//napis a= cislo
	cout << "bod b: "; //vypise bod b:
	cin >> b;//napis b= cislo
	cout << "bod c: "; //vypise bod c:
	cin >> c;//napis c= cislo;
	cout << "bod d: "; //vypise bod d:
	cin >> d;//napis d= cislo;
	
	c=c-d;
	dis=(pow(b,2))-4*a*c;
	x1=(-b + sqrt(dis))/(2*a);
	x2=(-b - sqrt(dis))/(2*a);

	if (dis==0)
	{
	cout<< "Diskriminant je roven 0, rovnice ma jedno reseni. X="<<x1<<endl;
	};
	if (dis<0)
	{
	cout<< "Diskriminant je mensi nez 0, rovnice nema reseni"<<endl;	
	};
	if (dis>0)
	{
	cout<< "Diskriminant je vetsi 0, rovnice ma dve reseni."<<endl;
	cout<< "x1= "<<x1<<endl;
	cout<< "x2= "<<x2<<endl;
	};
	
	cout <<"stiskni enter"<<endl;
	cin.get(); // ceka na stisk enteru
	cin.get();
	return 0;
}
