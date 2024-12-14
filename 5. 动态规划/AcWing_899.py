from typing import List

def minDistance(word1: str, word2: str) -> int:
    n, m = len(word1), len(word2)
    f = [[0] * (m + 1) for _ in range(n + 1)]
    f[0] = list(range(m + 1))

    for i, x in enumerate(word1):
        f[i + 1][0] = i + 1
        for j, y in enumerate(word2):
            if x == y:
                f[i + 1][j + 1] = f[i][j] 
            else:
                f[i + 1][j + 1] = min(f[i][j + 1], f[i + 1][j], f[i][j]) + 1

    return f[n][m]


if __name__ == "__main__":
    n, m = map(int, input().split())
    
    words = []
    for _ in range(n):
        word = input()
        words.append(word)
    
    for _ in range(m):
        s, limit = input().split()
        count = 0
        for word in words:
            if minDistance(s, word) <= int(limit):
                count += 1
        print(count)
