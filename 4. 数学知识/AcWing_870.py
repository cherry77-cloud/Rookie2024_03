from typing import List

def calculate_divisors_product(numbers: List[int], mod=10**9+7) -> int:
    from functools import reduce
    prime = dict()
    for x in numbers:
        for i in range(2, int(x**0.5) + 1):
            while x % i == 0: 
                x //= i; 
                prime[i] = prime.get(i, 0) + 1
        if x > 1: 
            prime[x] = prime.get(x, 0) + 1
    return reduce(lambda x, y: x * y % mod, (v + 1 for v in prime.values()), 1)


if __name__ == "__main__":
    n = int(input())
    numbers = list()
    for _ in range(n):
        numbers.append(int(input()))
    print(calculate_divisors_product(numbers))
