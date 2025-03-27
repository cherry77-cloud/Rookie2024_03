#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>

using namespace std;

int max_disjoint_intervals(vector<pair<int, int>>& intervals) {
    sort(intervals.begin(), intervals.end(), [](const auto& a, const auto& b) {
        return a.second < b.second;
    });

    int count = 0;
    int last_end = INT_MIN;

    for (const auto& interval : intervals) {
        if (interval.first > last_end) {
            last_end = interval.second;
            count++;
        }
    }
    return count;
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

    int ans = max_disjoint_intervals(intervals);
    cout << ans << endl;

    return 0;
}
