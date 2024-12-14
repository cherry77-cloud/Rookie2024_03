from typing import Tuple

def solve_linear_congruence(a: int, b: int, m: int) -> int:
    def extended_gcd(a: int, b: int) -> Tuple[int, int]:
        if b == 0:
            return 1, 0
        x1, y1 = extended_gcd(b, a % b)
        x, y = y1, x1 - (a // b) * y1
        return x, y
        
    from math import gcd
    d = gcd(a, m)
    if b % d != 0:
        return -1
    a, b, m = a // d, b // d, m // d
    x, y = extended_gcd(a, m)
    x = (x * b % m + m) % m
    return x


if __name__ == "__main__":
    n = int(input())
    for _ in range(n):
        a, b, m = map(int, input().split())
        result = solve_linear_congruence(a, b, m)
        if result != -1:
            print(result)
        else:
            print("impossible")
