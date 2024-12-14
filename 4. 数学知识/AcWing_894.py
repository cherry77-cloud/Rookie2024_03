from typing import List
from functools import lru_cache

def nim_game(pile_sizes: List[int]) -> bool:
    @lru_cache(maxsize=None)
    def sg(x: int) -> int:
        if x == 0:
            return 0
        return min(set(range(x + 1)) - {sg(i) ^ sg(j) for i in range(x) for j in range(i + 1)})

    result = 0
    for pile in pile_sizes:
        result ^= sg(pile)
    
    return result != 0

def main():
    n = int(input())
    pile_sizes = list(map(int, input().split()))

    is_first_player_win = nim_game(pile_sizes)
    print("Yes" if is_first_player_win else "No")

if __name__ == "__main__":
    main()
