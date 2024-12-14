from typing import Tuple
import math

def modular_inverse(a: int, p: int) -> int:
    def extended_gcd(a: int, b: int) -> Tuple[int, int]:
        if b == 0:
            return 1, 0
        x1, y1 = extended_gcd(b, a % b)
        x, y = y1, x1 - (a // b) * y1
        return x, y
        
    x, y = extended_gcd(a, p)
    return (x % p + p) % p


def modular_inverse_fermat(a: int, p: int) -> int:
    return pow(a, p-2, p)


def modular_inverse_euler(a: int, p: int) -> int:
    def phi(x: int) -> int:
        result, i = x, 2
        while i * i <= x:
            if x % i == 0:
                while x % i == 0: x //= i
                result -= result // i
            i += 1
        if x > 1: result -= result // x
        return result
    
    return pow(a, phi(p) - 1, p)


if __name__ == "__main__":
    n = int(input())
    for _ in range(n):
        a, b = map(int, input().split())
        if math.gcd(a, b) > 1:
            print("impossible")
        else:
            print(modular_inverse(a, b))
