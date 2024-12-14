from typing import List

class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])
        s = [[0] * (n + 1) for _ in range(m + 1)]
        for i, row in enumerate(matrix):
            for j, x in enumerate(row):
                s[i + 1][j + 1] = s[i + 1][j] + s[i][j + 1] - s[i][j] + x
        self.s = s

    # 返回左上角在 (r1,c1) 右下角在 (r2,c2) 的子矩阵元素和
    def sumRegion(self, r1: int, c1: int, r2: int, c2: int) -> int:
        return self.s[r2 + 1][c2 + 1] - self.s[r2 + 1][c1] - self.s[r1][c2 + 1] + self.s[r1][c1]


if __name__ == "__main__":
    n, m, q = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    num_matrix = NumMatrix(matrix)
    
    for _ in range(q):
        r1, c1, r2, c2 = map(int, input().split())
        print(num_matrix.sumRegion(r1 - 1, c1 - 1, r2 - 1, c2 - 1))
