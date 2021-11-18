#include <stdio.h>
#include <stdlib.h>

int main(int argc, char** argv) {


int kinosal[19][19]; //x,y souøadnice; poèítá se od 0 do 0+20=19
char i, j;
// Naplnìní teèkami
for (j = 0; j < 19; j++) // vnìjší cyklus
    for (i = 0; i < 19; i++) // vnitøní vyklus
        kinosal[j][i] = '.';
kinosal[9][9] = 'X'; // Prostredek
for (i = 9; i < 11; i++) 
{
for (i=8; i<11;i++)
{kinosal [i][10]='X';
	}
for (i=7; i<12;i++)
{kinosal [i][11]='X';
	}
for (i=6; i<13;i++)
{kinosal [i][12]='X';
	}
for (i=5; i<14;i++)
{kinosal [i][13]='X';
	}
for (i=4; i<15;i++)
{kinosal [i][14]='X';
	}
for (i=3; i<16;i++)
{kinosal [i][15]='X';
	}
for (i=2; i<17;i++)
{kinosal [i][16]='X';
	}
for (i=1; i<18;i++)
{kinosal [i][17]='X';
	}
for (i=0; i<19;i++)
{kinosal [i][18]='X';
	}
	
        kinosal[i][19] = '.';
}
for (i = 0; i < 19; i++) // Posledni radek
{
    kinosal[i][19] = '.'; //všechny souøadnice x, 20 y
}

for (j = 0; j < 19; j++)
{
        for (i = 0; i < 19; i++)
                printf("%c  ", kinosal[i][j]);
        printf("\n");
}
	return (EXIT_SUCCESS);
}
