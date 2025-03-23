#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

int main() {
    int n;
    cin >> n;

    vector<int> nums(n);
    for (int i = 0; i < n; ++i) {
        cin >> nums[i];
    }

    auto lengthOfLongestSubstring = [](const vector<int>& nums) -> int {
        int n = nums.size(), ans = 0, left = 0;
        unordered_map<int, int> cnt; // 维护从下标 left 到下标 right 的数字
        for (int right = 0; right < n; ++right) {
            int num = nums[right];
            cnt[num]++;
            while (cnt[num] > 1) { // 窗口内有重复数字
                cnt[nums[left]]--; // 移除窗口左端点数字
                left++; // 缩小窗口
            }
            ans = max(ans, right - left + 1); // 更新窗口长度最大值
        }
        return ans;
    };

    int result = lengthOfLongestSubstring(nums);
    cout << result << endl;

    return 0;
}
