#include <iostream>
#include <string>
using namespace std;

int main(void) {

cout << "Mala nasobilka pomoci dvou cyklu:" << endl;
for (int j = 1; j <= 10; j++)
{
    for (int i = 1; i <= 10; i++)
        cout << i * j << ' ';
    cout << endl;
}
cin.get();
	return 0;
}
