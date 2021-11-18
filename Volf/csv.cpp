#include <stdio.h>
#include <stdlib.h>
#include<iostream>
using namespace std;

int main (int argc, char** argv)
{
FILE * p_soubor = fopen("input.txt", "w");
    if (p_soubor == NULL)
    {
        printf("Soubor se nepodarilo otevrit pro zapis, zkontrolujte prosim opravneni.");
        return 1; // program konci
    }

   int i, j,temp;
   int a[10] = {10,2,0,14,43,25,18,1,5,45};
   cout <<"Vstup ...\n";
   for(i = 0; i<10; i++) {
      cout <<a[i]<<"\t";
   }
cout<<endl;
for(i = 0; i<10; i++) {
   for(j = i+1; j<10; j++)
   {
      if(a[j] < a[i]) {
         temp = a[i];
         a[i] = a[j];
         a[j] = temp;
      }
   }
}
cout <<"Serazene ...\n";
for(i = 0; i<10; i++) {
   cout <<a[i]<<"\t";
}
return 0;
}

