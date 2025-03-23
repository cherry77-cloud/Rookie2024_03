#include <iostream>
#include <vector>

using namespace std;

int main() 
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int target, n, m;
    cin >> n >> m >> target;

    vector<int> A(n), B(m);

    for (int i = 0; i < n; ++i) {
        cin >> A[i];
    }

    for (int i = 0; i < m; ++i) {
        cin >> B[i];
    }

    // 双指针算法
    for (int i = 0, j = m - 1; i < n; ++i) {
        while (j >= 0 && A[i] + B[j] > target) {
            j--; // 如果 A[i] + B[j] > target，移动 j 指针
        }
        if (j >= 0 && A[i] + B[j] == target) {
            cout << i << " " << j; // 找到目标值，输出下标
            break;
        }
    }

    return 0;
}
