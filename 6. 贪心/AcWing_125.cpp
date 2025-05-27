#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() 
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<pair<ll,ll>> items;
    items.reserve(n);

    // 读取输入并转换为 (total, weight)
    for (int i = 0; i < n; i++) {
        ll weight, strength;
        cin >> weight >> strength;
        ll total = weight + strength;
        items.emplace_back(total, weight);
    }

    // 按 total 升序排序
    sort(items.begin(), items.end(),
         [](const pair<ll,ll>& a, const pair<ll,ll>& b) {
             return a.first < b.first;
         });

    ll max_risk = LLONG_MIN;
    ll total_weight = 0;

    // 计算最大风险
    for (auto &p : items) {
        ll total  = p.first;
        ll weight = p.second;
        ll strength = total - weight;
        ll risk = total_weight - strength;
        max_risk = max(max_risk, risk);
        total_weight += weight;
    }

    cout << max_risk << "\n";
    return 0;
}
