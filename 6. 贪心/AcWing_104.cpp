#include <iostream>
#include <algorithm>
#include <cstring>

using namespace std;

const int N = 100010;

int a[N];

int main()
{
    int n;  cin >> n;
    
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    
    sort(a, a + n);
    
    int res = 0;
    for (int i = 0; i < n; i++) {
        res += a[i] - a[i >> 1];
    }
    
    cout << res << endl;
    return 0;
}
