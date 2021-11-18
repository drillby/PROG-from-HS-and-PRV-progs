#include <iostream>
#include <fstream>
using namespace std;

int writeFile () 
{
  ofstream myfile;
  myfile.open ("example.txt");
  myfile << "Writing this to a file.\n";
  myfile << "Writing this to a file.\n";
  myfile << "Writing this to a file.\n";
  myfile << "Writing this to a file.\n";
  myfile.close();
  return 0;
}

int main()
{
    writeFile();
}
