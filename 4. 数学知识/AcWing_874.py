from typing import List

def sieve_of_phi(n: int) -> int:
    phi = list(range(n + 1))
    
    for i in range(2, n + 1):
        if phi[i] == i:
            for j in range(i, n + 1, i):
                phi[j] = phi[j] // i * (i - 1)
                
    return phi


if __name__ == "__main__":
    n = int(input())
    phi = sieve_of_phi(n)
    print(sum(p for p in phi))
