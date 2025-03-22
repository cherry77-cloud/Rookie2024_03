#include <iostream>
#include <vector>

using namespace std;

vector<vector<int>> computePrefixSum(const vector<vector<int>>& matrix) 
{
    int rows = matrix.size();
    int cols = matrix[0].size();

    vector<vector<int>> prefix(rows + 1, vector<int>(cols + 1, 0));

    for (int i = 1; i <= rows; i++) {
        for (int j = 1; j <= cols; j++) {
            prefix[i][j] = prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1] + matrix[i - 1][j - 1];
        }
    }

    return prefix;
}

// 查询子矩阵的和
int regionSum(const vector<vector<int>>& prefix, int x1, int y1, int x2, int y2) 
{
    return prefix[x2 + 1][y2 + 1] - prefix[x1][y2 + 1] - prefix[x2 + 1][y1] + prefix[x1][y1];
}

int main() 
{
    int rows, cols, m;
    cin >> rows >> cols >> m;

    // 输入二维矩阵
    vector<vector<int>> matrix(rows, vector<int>(cols));
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            cin >> matrix[i][j];
        }
    }

    // 生成前缀和数组
    vector<vector<int>> prefix = computePrefixSum(matrix);

    // 查询子矩阵的和
    while (m--) {
        int x1, y1, x2, y2;
        cin >> x1 >> y1 >> x2 >> y2;
        
        x1 -= 1;
        x2 -= 1;
        y1 -= 1;
        y2 -= 1;

        cout << regionSum(prefix, x1, y1, x2, y2) << endl;
    }

    return 0;
}
