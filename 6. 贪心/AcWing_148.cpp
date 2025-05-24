#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

const int N = 20010;

int n, heap[N];

void up(int u) {
    while (u > 1 && heap[u] <= heap[u / 2]) {
        swap(heap[u], heap[u / 2]);
        u /= 2;
    }
}

void down(int u) {
    int t = u;
    if (u * 2 <= n && heap[t] >= heap[u * 2]) t = u * 2;
    if (u * 2 + 1 <= n && heap[t] >= heap[u * 2 + 1])  t = u * 2 + 1;
    if (u != t) {
        swap(heap[u], heap[t]);
        down(t);
    }
}

int main() {
    
    cin >> n;
    
    for (int i = 1; i <= n; ++i)  cin >> heap[i];
    
    for (int i = n / 2; i; --i)  down(i);
    
    int res = 0;
    while (n > 1) {
        int a = heap[1];
        heap[1] = heap[n--], down(1);
        int b = heap[1];
        heap[1] = heap[n--], down(1);
        res += a + b;
        heap[++n] = a + b; up(n);
    }
    
    cout << res << endl;
    
    return 0;
}
