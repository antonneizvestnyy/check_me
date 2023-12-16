//calculator
#include <iostream>
#include <cmath>

using namespace std;

int main() {
    int x = 3, y = 2;
    cin >> x;
    char oper = '+';
    cin >> oper;
    cin >> y;

    cout << "Operation result: \n";
    switch (oper) {
        case '+':
            cout << x + y;
            break;
        case '-':
            cout << x - y;
            break;
        case '*':
            cout << x * y;
            break;
        case '/':
            cout << x / y;
            break;
        case '%':
            cout << x % y;
            break;
        default:
            cout << "No such operation";
    }



return 0;
}
