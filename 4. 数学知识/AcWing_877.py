from typing import Tuple

def extended_gcd(a: int, b: int) -> Tuple[int, int]:
    if b == 0:
        return 1, 0
    x1, y1 = extended_gcd(b, a % b)
    x, y = y1, x1 - (a // b) * y1
    return x, y


if __name__ == "__main__":
    n = int(input())
    for _ in range(n):
        a, b = map(int, input().split())
        x, y = extended_gcd(a, b)
        print(f"{x} {y}")
