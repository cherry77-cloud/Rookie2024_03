from typing import List

def count_divisibles(n: int, primes: List[int]) -> int:
    m = len(primes)
    result = 0
    
    for i in range(1, 1 << m):
        subset_product = 1
        bits_count = bin(i).count('1')
        
        for j in range(m):
            if i & (1 << j):
                if subset_product > n // primes[j]:
                    subset_product = -1
                    break
                subset_product *= primes[j]

        if subset_product != -1:
            if bits_count % 2:
                result += n // subset_product
            else:
                result -= n // subset_product
    
    return result


if __name__ == "__main__":
    n, m = map(int, input().split())
    primes = list(map(int, input().split()))
    print(count_divisibles(n, primes))
