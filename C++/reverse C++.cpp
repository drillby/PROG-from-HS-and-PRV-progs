#include <iostream>
#include <algorithm>
using namespace std;

int main(void)
{

const int delkaPole = 5;
int pole[delkaPole] = { 1, 2, 3, 4, 5 };
reverse(pole, pole + delkaPole);
// pole = { 5, 4, 3, 2, 1 }
for (int i = 0; i < delkaPole; i++)
{
    cout << pole[i] << " ";
}
cin.get();

return 0;
}
