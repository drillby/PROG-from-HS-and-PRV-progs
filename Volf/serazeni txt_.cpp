#include <iostream>
#include <fstream>    
#include <cstdlib>    
 

int readInputFromFile(int input[]);
void displayArray(int input[], int size);
void bubbleSort(int input[], int n);

const char* inputFileName = "input.txt";

const short arraySize = 100;
 

int main() {
int input[arraySize] = { 0 }; // Set the contents of input array to 0.
int count = 0; // Variable to save the actual length of array.
 

count = readInputFromFile(input);
 
// Display unsorted or raw input data.
std::cout << "Input (" << count << " znaku): " << std::endl;
displayArray(input, count);
 
// Sort the input array using in-place bubble sort algorithm.
bubbleSort(input, count);
 
// Display the sorted output.
std::cout << "Serazeny output (" << count << " znaku): " << std::endl;
displayArray(input, count);
 
return 0;
}
 

 
void bubbleSort(int input[], int n) 
{
bool swapped = true;
for (int i = 0; i < n - 1 && swapped == true; i++) 
	{
	swapped = false;
	for (int j = 0; j < n - 1 - i; j++) 
		{
		if (input[j] > input[j + 1]) 
			{
			// Swap the elements.
			int temp = input[j];
			input[j] = input[j + 1];
			input[j + 1] = temp;
			swapped = true;
			}
		}
	}
}
 

 
int readInputFromFile(int input[]) {
std::ifstream in(inputFileName);
if (in.is_open() == false) {
std::cerr << "Nepodarilo se otevrit soubor!" << std::endl;
exit(1);
} else {
int count = 0;
while (!in.eof()) {
in >> input[count];
if (++count >= 100)
break;
}
in.close();
 
if (count >= 100) {
std::cerr << "Vstup prekracuje omezeni velikosti." << std::endl;
std::cerr << "Pouze " << arraySize << " znaku je povoleno! ";
std::cerr << "Ale je zde " << count + 1 << " znaku!" << std::endl;
std::cerr << std::endl;
exit(2);
}
return count;;
}
}
 

 
void displayArray(int input[], int size) {
for (int i = 0; i < size; i++)
std::cout << "\t" << *(input + i);
std::cout << std::endl;
}
