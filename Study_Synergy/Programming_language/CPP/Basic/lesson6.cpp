// Оператор присвоения
#include <iostream>
#include <string>
// #include <iomanip>

using namespace std;

int main() {
    string name;
    cin >> name;
    // Balex представим имя , нужно сделать 1 букву не заглавную
    // таблица аски, вычитаем через переменнюю цифру этой заглавной буквы на 1
    // получаем ответ
    name[0] = char((int)name[0] - (int)'A' + (int)'a');
    cout << name;

    return 0;
}