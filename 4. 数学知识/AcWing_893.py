from typing import List
from functools import lru_cache


def nim_game(allowed_moves: List[int], pile_sizes: List[int]) -> bool:
    @lru_cache(maxsize=None)
    def calculate_sg(pile_size: int) -> int:
        if pile_size == 0:
            return 0
            
        possible_moves = [move for move in allowed_moves if pile_size >= move]
        next_states = [calculate_sg(pile_size - move) for move in possible_moves]
        
        mex = 0
        while mex in next_states:
            mex += 1
        
        return mex

    xor_sum = 0
    for pile in pile_sizes:
        xor_sum ^= calculate_sg(pile)
    
    return xor_sum != 0


def main():
    k = int(input())
    s = list(map(int, input().split()))
    n = int(input())
    h = list(map(int, input().split()))

    result = nim_game(s, h)
    print("Yes" if result else "No")


if __name__ == "__main__":
    main()
