#include <iostream>
#include <cstdlib>
#include <ctime> 
using namespace std;

int main(int argc, char** argv)
{
int a;
int b;
int c;
int d;
int vysledek;

srand((unsigned)time(0));
a=rand() % 100+1;
cout<<a<<endl;

srand((unsigned)time(0));
b=rand() % 100-1;
cout<<b<<endl;

vysledek=a+b;
cout<<"Vysledek je"<<vysledek<<endl;
cin>>c;

if(c==vysledek)
	{
	cout<<"Tvuj vysledek"<<c<<endl;
	cout<<"Jsi skvely poctar..."<<endl;
	}
	
else	
	{
	cout<<"Tvuj vysledek"<<c<<endl;
	cout<<"Nauc se matiku..."<<endl;
	}
	
if(c==vysledek)
cin.get();
cin.get();
return 0;
}
