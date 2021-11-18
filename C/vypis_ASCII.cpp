#include <iostream>
using namespace std;

int main(){
    cout << "ASCII tabulka\n"<<endl;
    int i=0;
    int c;
    i=(int)c;
    while (i != 256){
    i++;
    c=(char)i;
	printf(" %d = %c\n", i, c);
    }
    return 0;
}
