#include <iostream>
#include <vector>

using namespace std;

// 构造差分数组, diff[i] 表示把下标 ≥i 的数都加上 diff[i]
vector<int> buildDiffArray(const vector<int>& arr) 
{
    int n = arr.size();
    vector<int> diff(n + 1, 0);
    diff[0] = arr[0];
    for (int i = 1; i < n; i++) {
        diff[i] = arr[i] - arr[i - 1];
    }
    return diff;
}

// 区间更新操作
void rangeUpdate(vector<int>& diff, int left, int right, int value) 
{
    diff[left] += value;
    diff[right + 1] -= value;
}

// 还原原数组
void restoreArray(vector<int>& diff) 
{
    for (int i = 1; i < diff.size(); i++) {
        diff[i] += diff[i - 1];
    }
}

int main() {
    int n, m;
    cin >> n >> m;

    // 输入原数组
    vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    // 构造差分数组
    vector<int> diff = buildDiffArray(arr);

    // 区间更新操作
    while (m--) {
        int left, right, value;
        cin >> left >> right >> value;  // 输入 left 和 right（1-based）
        left -= 1;  // 转换为 0-based
        right -= 1; // 转换为 0-based
        rangeUpdate(diff, left, right, value);  // 对区间 [left, right] 加上 value
    }

    // 还原原数组
    restoreArray(diff);

    // 输出结果
    for (int i = 0; i < n; i++) {
        cout << diff[i] << ' ';
    }

    return 0;
}
