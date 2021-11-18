#include <stdio.h>
#include <stdlib.h>

double faktorial(int n) // vytvoøení funkce faktorial
{
    if (n == 1)
        return 1;
    return n * faktorial(n - 1);
}
main() // samotný program
{
FILE * soubor1 = fopen("faktorial.txt", "w"); // vytvoøení txt souboru	

if (soubor1 == NULL) // kontrola pro otevøení  
	{
	 printf("Soubor se nepodaøilo otevøít pro zápis, zkontrolujte prosím oprávnìní.");
	 return 1;
	}

int n;
printf("Zadejte stupen faktorialu: \n");
scanf("%d",&n);

for(int i=1;i<=n;i++)
	{
     fprintf(soubor1,"%d!=%f \n",i, faktorial(i)); // vypsání do souboru
	}

if (fclose(soubor1) == EOF) // zavøení souboru 
    {
     printf("Soubor se nepodaøilo uzavøít.");
     return 1;
    }
    
return (EXIT_SUCCESS);

}
