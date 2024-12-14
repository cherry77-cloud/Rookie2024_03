from typing import List

def sum_of_divisors(numbers: List[int], modulus=10**9+7) -> int:
    from collections import defaultdict
    prime_counts = defaultdict(int)
    
    for num in numbers:
        for i in range(2, int(num**0.5) + 1):
            while num % i == 0:
                num //= i
                prime_counts[i] += 1
        if num > 1:
            prime_counts[num] += 1
    
    ans = 1
    for prime, count in prime_counts.items():
        divisor_sum = sum((pow(prime, i, modulus) for i in range(1, count + 1)), 1)
        ans = ans * divisor_sum % modulus
    
    return ans


if __name__ == "__main__":
    n = int(input())
    numbers = list()
    for _ in range(n):
        numbers.append(int(input()))
    print(sum_of_divisors(numbers))
