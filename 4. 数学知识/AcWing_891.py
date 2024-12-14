from typing import List

def can_win_nim(stones: List[int]) -> bool:
    ret = 0
    for stone in stones:
        ret ^= stone
    
    return ret != 0


if __name__ == "__main__":
    n = int(input())
    stones = list(map(int, input().split()))
    
    if can_win_nim(stones):
        print("Yes")
    else:
        print("No")
