from typing import List

class CombinationCalculator:
    def __init__(self, n: int) -> None:
        self.primes = []
        self.is_prime = [True] * (n + 1)
        self.sieve_primes(n)

    def sieve_primes(self, n: int) -> None:
        for i in range(2, n + 1):
            if self.is_prime[i]:
                self.primes.append(i)
            for prime in self.primes:
                if i * prime > n:
                    break
                self.is_prime[i * prime] = False
                if i % prime == 0:
                    break

    def count_factors(self, n: int, p: int) -> int:
        count = 0
        while n:
            n //= p
            count += n
        return count

    def calculate(self, a: int, b: int) -> List[int]:
        if b > a:
            return [0]

        sum_factors = [0] * len(self.primes)
        for i, prime in enumerate(self.primes):
            sum_factors[i] = self.count_factors(a, prime) - self.count_factors(b, prime) - self.count_factors(a - b, prime)

        result = [1]
        for i, prime in enumerate(self.primes):
            for _ in range(sum_factors[i]):
                result = self.mul(result, prime)
        
        return result[::-1]

    def mul(self, digits: List[int], x: int) -> List[int]:
        carry = 0
        for i in range(len(digits)):
            carry += digits[i] * x
            digits[i] = carry % 10
            carry //= 10
        while carry:
            digits.append(carry % 10)
            carry //= 10
        return digits


if __name__ == "__main__":
    a, b = map(int, input().split())
    calc = CombinationCalculator(a)
    result = calc.calculate(a, b)
    print(''.join(map(str, result)))
