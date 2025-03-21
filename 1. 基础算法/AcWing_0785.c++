#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void quickSort(vector<int>&, int, int);

int main() 
{
    int n;
    cin >> n;
    vector<int> arr(n);
    for (int i = 0; i < n; ++i) {
        cin >> arr[i];
    }
    quickSort(arr, 0, n - 1);
    
    for (int num : arr) {
        cout << num << " ";
    }
    return 0;
}

void quickSort(vector<int>& arr, int left, int right) 
{
    if (left >= right) return;  // 递归终止条件
    
    int pivot_index = (left + right) >> 1;  // 选择中间元素作为基准点
    int pivot_value = arr[pivot_index];
    int i = left - 1, j = right + 1;  // 双指针
    
    while (i < j) {
        while (arr[++i] < pivot_value);   // 左指针向右移动
        while (arr[--j] > pivot_value);   // 右指针向左移动
        if (i < j) std::swap(arr[i], arr[j]);  // 交换不满足条件的元素
    }
    
    quickSort(arr, left, j);      // 递归处理左区间
    quickSort(arr, j + 1, right); // 递归处理右区间
}
