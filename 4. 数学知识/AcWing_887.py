from typing import Tuple, List

class LucasTheorem:
    def __init__(self, mod: int) -> None:
        self.mod = mod
        self.inv = [1] * (mod + 1)
        for i in range(2, mod):
            self.inv[i] = (self.mod - self.mod // i) * self.inv[self.mod % i] % self.mod

    def combination(self, a: int, b: int) -> int:
        if b > a:
            return 0
        result = 1
        for i in range(1, b + 1):
            numerator = (a - i + 1) % self.mod
            denominator_inv = self.inv[i]
            result = result * numerator % self.mod * denominator_inv % self.mod
        return result

    def lucas(self, a: int, b: int) -> int:
        if a < self.mod and b < self.mod:
            return self.combination(a, b)
        return (self.combination(a % self.mod, b % self.mod) * self.lucas(a // self.mod, b // self.mod) % self.mod)


if __name__ == "__main__":
    n = int(input())

    for _ in range(n):
        a, b, p = map(int, input().split())
        lucas_calculator = LucasTheorem(mod=p)
        print(lucas_calculator.lucas(a, b))
