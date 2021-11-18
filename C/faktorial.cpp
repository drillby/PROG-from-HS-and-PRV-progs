#include <stdio.h>
#include <stdlib.h>



double faktorial(int n) // vytvoøená funkce
{
    if (n == 1)
        return 1;
    return n * faktorial(n - 1);
}

main()
{
int n;
printf("Zadejte stupen faktorialu:");
scanf("%d",&n);
for(int i=1;i<=n;i++)
	{
	 printf("%3d!=%190.01f \n",i, faktorial(i)); 	
	}
}

