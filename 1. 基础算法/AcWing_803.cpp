#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<vector<int>> merge(vector<vector<int>>& intervals) 
{
    sort(intervals.begin(), intervals.end());
    vector<vector<int>> ans;
    for (auto& p : intervals) {
        if (!ans.empty() && p[0] <= ans.back()[1]) {
            // 如果当前区间与结果中的最后一个区间有交集，则合并
            ans.back()[1] = max(ans.back()[1], p[1]);
        } else {
            // 否则，将当前区间加入结果
            ans.emplace_back(p);
        }
    }
    return ans;
}

int main() 
{
    int n;
    cin >> n;

    vector<vector<int>> intervals;
    for (int i = 0; i < n; ++i) {
        int l, r;
        cin >> l >> r;
        intervals.push_back({l, r});
    }

    vector<vector<int>> merged = merge(intervals);
    cout << merged.size() << endl;

    return 0;
}
