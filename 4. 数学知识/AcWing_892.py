from typing import List

def can_first_player_win(stairs: List[int]) -> bool:
    ret = 0
    for i, stair in enumerate(stairs):
        if i % 2 == 0:
            ret ^= stair
    return ret != 0


if __name__ == "__main__":
    n = int(input())
    stones = list(map(int, input().split()))
    
    if can_first_player_win(stones):
        print("Yes")
    else:
        print("No")
