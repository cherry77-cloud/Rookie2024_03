from typing import List

class DiffMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.n = len(matrix)
        self.m = len(matrix[0]) if self.n > 0 else 0
        self.diff = [[0] * (self.m + 1) for _ in range(self.n + 1)]
        self.populate(matrix)
    
    def populate(self, matrix: List[List[int]]) -> None:
        for r in range(self.n):
            for c in range(self.m):
                self.update(r, c, r, c, matrix[r][c])
    
    def update(self, r1: int, c1: int, r2: int, c2: int, value: int) -> None:
        self.diff[r1][c1] += value
        if c2 + 1 < self.m:
            self.diff[r1][c2 + 1] -= value
        if r2 + 1 < self.n:
            self.diff[r2 + 1][c1] -= value
        if r2 + 1 < self.n and c2 + 1 < self.m:
            self.diff[r2 + 1][c2 + 1] += value

    def reconstruct(self):
        final = [[0] * self.m for _ in range(self.n)]
        for r in range(self.n):
            for c in range(self.m):
                if r > 0:
                    self.diff[r][c] += self.diff[r - 1][c]
                if c > 0:
                    self.diff[r][c] += self.diff[r][c - 1]
                if r > 0 and c > 0:
                    self.diff[r][c] -= self.diff[r - 1][c - 1]
                final[r][c] = self.diff[r][c]
        return final


if __name__ == "__main__":
    n, m, q = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    
    diff_matrix = DiffMatrix(matrix)
    
    for _ in range(q):
        r1, c1, r2, c2, val = map(int, input().split())
        diff_matrix.update(r1 - 1, c1 - 1, r2 - 1, c2 - 1, val)
    
    mat = diff_matrix.reconstruct()
    
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            print(mat[i][j], end=" ")
        print()
