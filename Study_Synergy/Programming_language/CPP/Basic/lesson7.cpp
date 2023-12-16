#include <iostream>
#include <string>
#include <cmath>

using namespace std;

int main() {
    int x, y;
    cin >> x >> y;
    if (x > y) {
        cout << "x < y";
    }
    else {
        if  (x == y) {
            cout << "x = y";
        }
        else {
            cout << "x > y";
        }
        cout << "\n";
        cout << ((x < y) ? "x < y" : "x >= y");
        // тернарный оператор
        // идентичная запись

       
    }

    return 0;
}