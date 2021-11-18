#include <iostream>
#include <algorithm>
#include <ctime>
using namespace std;

int main(void)
{

const int delkaPole = 50;
int pole[delkaPole];
srand(unsigned(time(0))); // inicializuje generátor náhodných èísel
///////////////////////////

for (int i = 0; i < delkaPole; i++) // cisla od 1 do 100
   {
    pole[i]=rand() % 100+1; 
   }

///////////////////////////////////
cout<<"Nesetridene pole"<<endl;
cout<<endl;  
for (int i = 0; i < delkaPole; i++) // vypise pole
   {
    cout << pole[i] << " ";
   }
cout<<endl;

//////////////////////////////////////
cout<<"Setridene pole"<<endl;
cout<<endl; 
sort(pole, pole + delkaPole); // srovna pole od nejmensiho po nejvetsi

for (int i = 0; i < delkaPole; i++)
   {
    cout << pole[i] << " ";
   }
cout<<endl;
   
//////////////////////////////
cout<<"Vypsane naopak pole"<<endl;
cout<<endl;
reverse(pole, pole + delkaPole); // vypise naopak
cout<<endl;
for (int i = 0; i < delkaPole; i++)
   {
    cout << pole[i] << " ";
   }
cout<<endl;
///////////////////////////////////

cin.get();

return 0;
}

