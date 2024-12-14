from typing import List

def longestCommonSubsequence(text1: str, text2: str) -> int:
    n, m = len(text1), len(text2)
    f = [[0] * (m + 1) for _ in range(n + 1)]
    for i, x in enumerate(text1):
        for j, y in enumerate(text2):
            if x == y:
                f[i + 1][j + 1] = f[i][j] + 1 
            else:
                f[i + 1][j + 1] = max(f[i][j + 1], f[i + 1][j])

    return f[n][m]


if __name__ == "__main__":
    n, m = map(int, input().split())
    a = input()
    b = input()
    print(longestCommonSubsequence(a, b))
