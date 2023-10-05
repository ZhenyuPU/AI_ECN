#include <iostream>
#include <cstdint>
using namespace std;
int main() {
    int x = 16777218;
    int* p; // 声明p为int64_t指针
    int* q; // 声明q为int64_t指针

    p = &x;

    q = &x;

    cout << "p: " << *p << endl; // 输出p指向的值
    cout << "x: " << x << endl;  // 输出x的值

    return 0;
}
