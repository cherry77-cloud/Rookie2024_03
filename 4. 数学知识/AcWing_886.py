from typing import Tuple, List

class Combinatorics:
    def __init__(self, max_n=100010, mod=10**9+7):
        self.mod = mod
        self.fact, self.inv_fact = self.prepare_factorials(max_n, mod)

    def modular_inverse(self, a: int, p: int) -> int:
        def extended_gcd(a: int, b: int) -> Tuple[int, int]:
            if b == 0:
                return 1, 0
            x1, y1 = extended_gcd(b, a % b)
            x, y = y1, x1 - (a // b) * y1
            return x, y
            
        x, y = extended_gcd(a, p)
        return (x % p + p) % p

    def prepare_factorials(self, max_n: int, mod: int) -> Tuple[List[int], List[int]]:
        fact = [1] * (max_n + 1)
        inv_fact = [1] * (max_n + 1)
        for i in range(1, max_n + 1):
            fact[i] = fact[i - 1] * i % mod
            inv_fact[i] = inv_fact[i - 1] * self.modular_inverse(i, mod) % mod
        return fact, inv_fact

    def combination(self, n: int, k: int) -> int:
        if k > n:
            return 0
        return (self.fact[n] * self.inv_fact[k] % self.mod * self.inv_fact[n - k] % self.mod)


if __name__ == "__main__":
    n = int(input())
    comb_calculator = Combinatorics()
    for _ in range(n):
        n, k = map(int, input().split())
        print(comb_calculator.combination(n, k))
