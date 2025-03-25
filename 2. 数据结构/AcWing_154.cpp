#include <iostream>
#include <vector>
#include <algorithm>
#include <deque>

using namespace std;

vector<pair<int, int>> slidingWindowMinMax(const vector<int>& nums, int k) {
    vector<pair<int, int>> result;
    deque<int> min_q, max_q;
    
    for (int i = 0; i < nums.size(); ++i) {
        // 1. 先入队 - 维护单调性
        while (!min_q.empty() && nums[min_q.back()] >= nums[i]) {
            min_q.pop_back();
        }
        min_q.push_back(i);
        
        while (!max_q.empty() && nums[max_q.back()] <= nums[i]) {
            max_q.pop_back();
        }
        max_q.push_back(i);
        
        // 2. 后出队 - 移除不在窗口中的元素
        while (!min_q.empty() && min_q.front() <= i - k) {
            min_q.pop_front();
        }
        while (!max_q.empty() && max_q.front() <= i - k) {
            max_q.pop_front();
        }
        
        // 3. 记录答案 - 当窗口形成时
        if (i >= k - 1) {
            result.emplace_back(nums[min_q.front()], nums[max_q.front()]);
        }
    }
    
    return result;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    
    int n, k;
    cin >> n >> k;
    vector<int> nums(n);
    
    for (int i = 0; i < n; ++i) {
        cin >> nums[i];
    }
    
    auto minmax_pairs = slidingWindowMinMax(nums, k);
    
    for (const auto& p : minmax_pairs) {
        cout << p.first << " ";
    }
    cout << "\n";
    
    for (const auto& p : minmax_pairs) {
        cout << p.second << " ";
    }
    cout << "\n";
    
    return 0;
}
