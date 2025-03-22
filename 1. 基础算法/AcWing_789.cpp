#include <iostream>
#include <vector>
using namespace std;

int main() 
{
    int n, t;
    cin >> n >> t;
    vector<int> nums(n);
    for (int i = 0; i < n; i++) {
        cin >> nums[i];
    }

    // 查找第一个大于等于 target 的元素的下标
    auto find_first_blue = [](const vector<int>& nums, int target) {
        int left = 0, right = nums.size() - 1;
        while (left < right) {
            int pivot = (left + right) / 2;
            if (nums[pivot] >= target) {
                right = pivot;
            } else {
                left = pivot + 1;
            }
        }
        return left;
    };

    // 查找最后一个小于等于 target 的元素的下标
    auto find_last_red = [](const vector<int>& nums, int target) {
        int left = 0, right = nums.size() - 1;
        while (left < right) {
            int pivot = (left + right + 1) / 2;
            if (nums[pivot] <= target) {
                left = pivot;
            } else {
                right = pivot - 1;
            }
        }
        return left;
    };

    while (t--) {
        int x;
        cin >> x;
        int l = find_first_blue(nums, x);
        int r = find_last_red(nums, x);
        if (nums[l] != x) {
            cout << "-1 -1" << endl;
        } else {
            cout << l << " " << r << endl;
        }
    }

    return 0;
}
