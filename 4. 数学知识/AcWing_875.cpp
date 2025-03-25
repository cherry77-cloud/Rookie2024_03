#include <iostream>

using namespace std;

typedef long long ll;

ll qmi(ll a, ll b, ll c) {
    ll ans = 1 % c;
    while (b) {
        if (b & 1)  ans = ans * a % c;
        b >>= 1;
        a = a * a % c;
    }
    return ans;
}

int main() {
    
    int n;  cin >> n;
    
    while (n--) {
        int a, b, c;  cin >> a >> b >> c;
        cout << qmi(a, b, c) << endl;
    }
    return 0;
}
