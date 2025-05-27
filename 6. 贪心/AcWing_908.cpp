#include <bits/stdc++.h>
using namespace std;

int interval_select(vector<pair<int,int>>& intervals) 
{
    // 按右端点升序排序
    sort(intervals.begin(), intervals.end(),
         [](const pair<int,int>& a, const pair<int,int>& b) {
             return a.second < b.second;
         });

    int cnt = 0;
    int last = INT_MIN;  // 上一次选的点

    for (auto &iv : intervals) {
        int start = iv.first;
        int end   = iv.second;
        // 如果当前区间未被覆盖，则选取 end
        if (start > last) {
            last = end;
            cnt++;
        }
    }
    return cnt;
}

int main() 
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<pair<int,int>> intervals(n);
    for (int i = 0; i < n; i++) {
        cin >> intervals[i].first >> intervals[i].second;
    }

    int ans = interval_select(intervals);
    cout << ans << "\n";
    return 0;
}
