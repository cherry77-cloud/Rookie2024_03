#include <iostream>
#include <vector>

using namespace std;

int main() 
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;

    vector<int> a(n), b(m);

    for (int i = 0; i < n; ++i) cin >> a[i];
    for (int j = 0; j < m; ++j) cin >> b[j];

    int i = 0, j = 0;
    while (i < n && j < m) {
        if (a[i] == b[j]) {
            i++;
        }
        j++;
    }

    if (i == n) {
        cout << "Yes" << endl; // a 是 b 的子序列
    } else {
        cout << "No" << endl; // a 不是 b 的子序列
    }

    return 0;
}
