#include <iostream>
#include <algorithm>
using namespace std;

int main(void)
{

const int delkaPole = 5;
int pole[delkaPole] = { 1, 2, 3, 4, 5 };
int pole2[delkaPole] = { 0, 0, 0, 0, 0 };
copy(pole, pole + delkaPole, pole2);
// pole = { 1, 2, 3, 4, 5 }, pole2 = { 1, 2, 3, 4, 5 }
for (int i = 0; i < delkaPole; i++)
{
    cout << pole[i] << "->" << pole2[i] << " ";
}
cin.get();

return 0;
}
