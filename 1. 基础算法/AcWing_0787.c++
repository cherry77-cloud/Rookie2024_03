#include <iostream>
#include <vector>

using namespace std;

void mergeSort(vector<int>&, int, int);

int main() 
{
    int n;
    cin >> n;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    
    mergeSort(arr, 0, n - 1);
    
    for (const auto& num : arr) {
        cout << num << " ";
    }
    
    return 0;
}

void mergeSort(vector<int>& arr, int left, int right) 
{
    if (left >= right) return;  // 递归终止条件
    
    int mid = left + (right - left) / 2;
    mergeSort(arr, left, mid);           // 递归排序左半部分
    mergeSort(arr, mid + 1, right);      // 递归排序右半部分
    
    // 合并临时数组
    vector<int> tmp(right - left + 1);
    int i = left, j = mid + 1, k = 0;
    
    while (i <= mid && j <= right) {
        if (arr[i] <= arr[j]) {
            tmp[k++] = arr[i++];
        } else {
            tmp[k++] = arr[j++];
        }
    }
    
    // 处理剩余元素
    while (i <= mid) tmp[k++] = arr[i++];
    while (j <= right) tmp[k++] = arr[j++];
    
    // 将临时数组拷贝回原数组
    for (int p = 0; p < k; p++) {
        arr[left + p] = tmp[p];
    }
}
