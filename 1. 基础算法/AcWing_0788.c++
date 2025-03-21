#include <iostream>
#include <vector>

using namespace std;

long long int countInversionPairs(vector<int>&, int, int);

int main() 
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n;
    cin >> n;
    vector<int> nums(n);
    for (int i = 0; i < n; i++) {
        cin >> nums[i];
    }
    
    long long inversionPairs = countInversionPairs(nums, 0, n - 1);
    cout << inversionPairs << endl;
    
    return 0;
}

long long countInversionPairs(vector<int>& nums, int left, int right) 
{
    if (left >= right) return 0;  // 递归终止条件
    
    int mid = left + (right - left) / 2;  // 计算中间点
    long long result = countInversionPairs(nums, left, mid) + 
                       countInversionPairs(nums, mid + 1, right);  // 递归计算左右子数组的逆序对
    
    // 合并临时数组
    vector<int> tmp(right - left + 1);
    int i = left, j = mid + 1, k = 0;
    
    while (i <= mid && j <= right) {
        if (nums[i] <= nums[j]) {
            tmp[k++] = nums[i++];
        } else {
            tmp[k++] = nums[j++];
            result += mid - i + 1;  // 统计逆序对
        }
    }
    
    // 处理剩余元素
    while (i <= mid) tmp[k++] = nums[i++];
    while (j <= right) tmp[k++] = nums[j++];
    
    // 将临时数组拷贝回原数组
    for (int p = 0; p < k; p++) {
        nums[left + p] = tmp[p];
    }
    
    return result;
}
