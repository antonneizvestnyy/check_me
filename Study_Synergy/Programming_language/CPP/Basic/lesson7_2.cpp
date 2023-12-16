//среднее число из 3х значений

#include <iostream>
#include <cmath>

using namespace std;

int main() {
    int x, y, z;
    cin >> x >> y >> z;
    int mi = min(x, min(y, z));
    int ma = max(x, max(y, z));
    int midle = x + y + z - ma - mi;
    if (x == midle) {
        cout << "Среднее число 1";
    }
    else if (y == midle) {
        cout << "Среднее число 2";
    }
    else {
        cout << "Среднее число 3";
    }

return 0;
}