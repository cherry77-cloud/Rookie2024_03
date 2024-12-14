from typing import List

def sieve_of_eratosthenes(n: int) -> List[int]:
    is_prime = [True] * (n + 1)
    
    for p in range(2, int(n**0.5) + 1):
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
                
    primes = [p for p in range(2, n + 1) if is_prime[p]]
    return primes


def sieve_of_euler(n: int) -> List[int]:
    vis = [False] * (n + 1)
    primes = []
    for i in range(2, n + 1):
        if not vis[i]: primes.append(i)
        for j in primes:
            if j * i > n: break
            vis[j * i] = True
            if i % j == 0: break
    return primes


if __name__ == "__main__":
    n = int(input())
    primes = sieve_of_euler(n)
    print(len(primes))
