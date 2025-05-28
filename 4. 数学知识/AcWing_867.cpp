#include <iostream>

using namespace std;

int main() {
    
    int n;  cin >> n;
    
    while (n--) {
        int x;  cin >> x;
        
        for (int i = 2; i <= x / i; ++i) {
            int cnt = 0;
            if (x % i == 0) {
                while (x % i == 0)  x /= i, cnt++;
                cout << i << " " << cnt << endl;
            }
        }
        
        if (x > 1)  cout << x << " " << 1 << endl;
        puts("");
    }
    
    return 0;
}
