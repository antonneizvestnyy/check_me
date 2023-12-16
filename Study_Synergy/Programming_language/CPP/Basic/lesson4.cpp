// типы данных
#include <iostream>
#include <string>
#include <iomanip>

using namespace std;
// namespace
enum Color { 
    red,
    white,
    brown,
    black

};

struct Animals {
    int legs = 4;
    Color color = black;
    string name = "";
};

int main() {
    Animals cat = {4, white, "Barsic"};
    cout << cat.legs << ' ' << cat.color << ' ' << cat.name;
}


