#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

int interval_group(vector<pair<int, int>>& intervals) {
    sort(intervals.begin(), intervals.end());
    priority_queue<int, vector<int>, greater<int>> heap;
    
    for (const auto& interval : intervals) {
        if (!heap.empty() && heap.top() < interval.first) {
            heap.pop();
            heap.push(interval.second);
        } else {
            heap.push(interval.second);
        }
    }
    
    return heap.size();
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n;
    cin >> n;
    
    vector<pair<int, int>> intervals;
    for (int i = 0; i < n; ++i) {
        int a, b;
        cin >> a >> b;
        intervals.emplace_back(a, b);
    }
    
    int ans = interval_group(intervals);
    cout << ans << endl;
    
    return 0;
}
