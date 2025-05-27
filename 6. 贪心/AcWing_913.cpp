#include <bits/stdc++.h>
using namespace std;

int main() 
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<long long> t(n);
    for (int i = 0; i < n; i++) {
        cin >> t[i];
    }

    // 1. 升序排序
    sort(t.begin(), t.end());

    // 2. 计算累加等待时间
    long long total_wait = 0;
    long long prefix = 0;  // S_k 表示前 k 个打水时间之和
    for (int i = 0; i < n; i++) {
        total_wait += prefix;
        prefix += t[i];
    }

    // 输出结果
    cout << total_wait << "\n";
    return 0;
}
