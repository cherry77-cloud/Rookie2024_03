from functools import lru_cache
from typing import List

def longest_skiing_path(n: int, m: int, matrix: List[List[int]]) -> int:
    @lru_cache(None)
    def dp(x, y):
        max_length = 1
        for nx, ny in (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1):
            if 0 <= nx < n and 0 <= ny < m and matrix[x][y] > matrix[nx][ny]:
                max_length = max(max_length, dp(nx, ny) + 1)
        return max_length

    result = 0
    for i in range(n):
        for j in range(m):
            result = max(result, dp(i, j))
    return result


if __name__ == "__main__":
    n, m = map(int, input().split())
    matrix = []
    for _ in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)
    print(longest_skiing_path(n, m, matrix))
