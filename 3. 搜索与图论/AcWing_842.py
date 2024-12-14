from typing import List

def dfs(current: int, used: int, permutation: List[int]) -> None:
    if current == n:
        print(" ".join(map(str, permutation)))
        return
    
    for i in range(1, n + 1):
        if not (used & (1 << i)):
            dfs(current + 1, used | (1 << i), permutation + [i])


if __name__ == "__main__":
    n = int(input())
    dfs(0, 0, [])
