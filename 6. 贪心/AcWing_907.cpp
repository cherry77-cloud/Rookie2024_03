#include <bits/stdc++.h>
using namespace std;

int min_intervals_to_cover_segment(int s, int t, vector<pair<int,int>>& intervals) 
{
    if (s == t) {
        for (auto &iv : intervals) {
            if (iv.first <= s && s <= iv.second) {
                return 1;
            }
        }
        return -1;
    }

    // 过滤
    vector<pair<int,int>> filtered;
    filtered.reserve(intervals.size());
    for (auto &iv : intervals) {
        if (iv.first <= t && iv.second >= s) {
            filtered.push_back(iv);
        }
    }

    // 按 起点升序，终点降序 排序
    sort(filtered.begin(), filtered.end(),
         [](auto &a, auto &b) {
             if (a.first != b.first) 
                 return a.first < b.first;
             return a.second > b.second;
         });

    int count = 0;
    int current_end = s;
    int max_end = s;
    int idx = 0;
    int n = filtered.size();

    // 贪心扫描
    while (current_end < t) {
        bool found = false;
        while (idx < n && filtered[idx].first <= current_end) {
            max_end = max(max_end, filtered[idx].second);
            found = true;
            idx++;
        }
        if (!found) {
            return -1;
        }
        current_end = max_end;
        count++;
        if (current_end >= t) break;
    }

    return count;
}

int main() 
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int s, t;
    cin >> s >> t;
    int n;
    cin >> n;
    vector<pair<int,int>> intervals(n);
    for (int i = 0; i < n; i++) {
        cin >> intervals[i].first >> intervals[i].second;
    }

    int ans = min_intervals_to_cover_segment(s, t, intervals);
    cout << ans << "\n";
    return 0;
}
