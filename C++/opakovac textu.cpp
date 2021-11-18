#include <iostream>
#include <string>
using namespace std;

int main(void)
{
    cout << "Ahoj, jsem virtualni papousek Lora, rad opakuji!" << endl;
    cout << "Napis neco: " << endl;
    string vstup;  //nadefinuje vstup
    cin >> vstup; // cin >> vstup = scanf
    string vystup;
    vystup = vstup + ", " + vstup + "!"; // zopakujue +, zopakuje +!
    cout << vystup << endl; // cout<<=printf, << endl konec øádku
    cin.get(); cin.get();
    return 0;
}


