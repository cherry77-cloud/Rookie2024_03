from typing import Tuple

class CatalanCalculator:
    def __init__(self, mod: int = 10**9 + 7):
        self.mod = mod
    
    def modular_inverse(self, a: int, p: int) -> int:
        def extended_gcd(a: int, b: int) -> Tuple[int, int]:
            if b == 0:
                return 1, 0
            x1, y1 = extended_gcd(b, a % b)
            x, y = y1, x1 - (a // b) * y1
            return x, y
            
        x, y = extended_gcd(a, p)
        return (x % p + p) % p

    def catalan_combinatorial(self, n: int) -> int:
        catalan = 1
        for i in range(1, n + 1):
            numerator = (2 * n - i + 1) % self.mod
            denominator_inv = self.modular_inverse(i, self.mod)
            catalan = catalan * numerator % self.mod * denominator_inv % self.mod
        return catalan * self.modular_inverse(n + 1, self.mod) % self.mod

    def catalan_formula(self, n: int) -> int:
        catalan = 1
        for i in range(2, n + 1):
            catalan = (catalan * (2 * (2 * i - 1) % self.mod) * self.modular_inverse(i + 1, self.mod)) % self.mod
        return catalan

        
if __name__ == "__main__":
    n = int(input())
    catalan = CatalanCalculator()
    print(catalan.catalan_combinatorial(n))
