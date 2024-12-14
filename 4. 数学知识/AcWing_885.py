from typing import List

def pascal_triangle(max_n=2010, mod=10**9+7) -> List[int]:
    c = [[0] * (max_n + 1) for _ in range(max_n + 1)]

    for i in range(max_n + 1):
        for j in range(i + 1):
            if j == 0:
                c[i][j] = 1
            else:
                c[i][j] = (c[i - 1][j] + c[i - 1][j - 1]) % mod
    
    return c


if __name__ == "__main__":
    n = int(input())
    c = pascal_triangle()
    for _ in range(n):
        a, b = map(int, input().split())
        print(c[a][b])
