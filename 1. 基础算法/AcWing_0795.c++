#include <iostream>
#include <vector>

using namespace std;

vector<int> computePrefixSum(const vector<int>& nums) 
{
    int n = nums.size();
    vector<int> prefix(n + 1, 0);   // prefix[i] 表示原数组前 i 个元素的和
    for (int i = 1; i <= n; i++) {
        prefix[i] = prefix[i - 1] + nums[i - 1];
    }
    return prefix;
}

int rangeSum(const vector<int>& prefix, int l, int r) 
{
    return prefix[r + 1] - prefix[l];
}

int main() {
    int n, m;
    cin >> n >> m;

    vector<int> nums(n);
    for (int i = 0; i < n; i++) {
        cin >> nums[i];
    }

    vector<int> prefix = computePrefixSum(nums);

    while (m--) {
        int l, r;
        cin >> l >> r;
        l -= 1;
        r -= 1;
        cout << rangeSum(prefix, l, r) << endl;
    }

    return 0;
}
