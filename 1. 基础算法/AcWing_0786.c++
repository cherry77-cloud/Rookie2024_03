#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int findKthElement(vector<int>&, int, int, int);

int main() 
{
    int n, k;
    cin >> n >> k;
    vector<int> nums(n);
    for (int i = 0; i < n; ++i) {
        cin >> nums[i];
    }
    
    int result = findKthElement(nums, 0, n - 1, k);
    cout << result << endl;
    
    return 0;
}


int findKthElement(vector<int>& nums, int left, int right, int k) 
{
    if (left == right) return nums[left];  // 递归终止条件
    
    int pivot_index = (left + right) >> 1;  // 选择中间元素作为基准点
    int pivot_value = nums[pivot_index];
    int i = left - 1, j = right + 1;  // 双指针
    
    while (i < j) {
        while (nums[++i] < pivot_value);    // 左指针向右移动
        while (nums[--j] > pivot_value);    // 右指针向左移动
        if (i < j) swap(nums[i], nums[j]);  // 交换不满足条件的元素
    }
    
    int left_partition_size = j - left + 1;  // 左分区的元素个数
    if (left_partition_size >= k) {
        return findKthElement(nums, left, j, k);  // 在左分区中查找
    }
    return findKthElement(nums, j + 1, right, k - left_partition_size);  // 在右分区中查找
}
