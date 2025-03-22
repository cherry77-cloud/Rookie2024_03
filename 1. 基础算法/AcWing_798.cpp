#include <iostream>
#include <vector>

using namespace std;

// 子矩阵更新操作
void regionUpdate(vector<vector<int>>& diff, int x1, int y1, int x2, int y2, int value) 
{
    diff[x1][y1] += value;          // 左上角加上 value
    diff[x1][y2 + 1] -= value;      // 右上角减去 value
    diff[x2 + 1][y1] -= value;      // 左下角减去 value
    diff[x2 + 1][y2 + 1] += value;  // 右下角加上 value
}

// 还原原数组
void restoreArray(vector<vector<int>>& diff, int n, int m) 
{
    for (int i = 1; i < n; i++) {
        for (int j = 0; j < m; j++) {
            diff[i][j] += diff[i - 1][j];  // 从上到下累加
        }
    }
    for (int j = 1; j < m; j++) {
        for (int i = 0; i < n; i++) {
            diff[i][j] += diff[i][j - 1];  // 从左到右累加
        }
    }
}

int main() 
{
    int n, m, q;
    cin >> n >> m >> q;

    // 输入原数组
    vector<vector<int>> arr(n, vector<int>(m, 0));  // 原数组大小为 n x m（下标从 0 开始）
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> arr[i][j];
        }
    }

    // 初始化差分数组
    vector<vector<int>> diff(n + 1, vector<int>(m + 1, 0));  // 差分数组大小为 n+1 x m+1
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            regionUpdate(diff, i, j, i, j, arr[i][j]);  // 初始化差分数组
        }
    }

    // 子矩阵更新操作
    while (q--) {
        int x1, y1, x2, y2, value;
        cin >> x1 >> y1 >> x2 >> y2 >> value;
        x1 -= 1;  // 转换为从 0 开始的下标
        y1 -= 1;
        x2 -= 1;
        y2 -= 1;
        regionUpdate(diff, x1, y1, x2, y2, value);  // 对子矩阵 [x1, y1] 到 [x2, y2] 加上 value
    }

    // 还原原数组
    restoreArray(diff, n, m);

    // 输出结果
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cout << diff[i][j] << ' ';
        }
        cout << endl;
    }

    return 0;
}
