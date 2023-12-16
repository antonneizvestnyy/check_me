#include <iostream>

using namespace std;


int main()
{
    string name;
    cout << "Enter your name: \n";
    cin >> name;
    string surname;
    cout << "Enter your surname: \n";
    cin >> surname;
    int age;
    cout << "Enter your age: \n";
    cin >> age;
    cout << "Your name is " << name;
    cout << "\nYour surname is " << surname;
    cout << "\nYour age is " << age << "years old!";
}