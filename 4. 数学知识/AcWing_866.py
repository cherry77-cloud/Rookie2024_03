from typing import List

def is_prime(n: int) -> bool:
    return n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))


def miller_rabin(n: int, k=10) -> bool:
    import random
    if n <= 1: return False
    if n in (2, 3): return True
    if n % 2 == 0: return False
    
    r, d = 0, n - 1
    while d % 2 == 0:
        d //= 2
        r += 1

    def witness(a: int) -> bool:
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            return False
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                return False
        return True

    return not any(witness(random.randint(2, n - 2)) for _ in range(k))
    
    
def main():
    n = int(input())
    for _ in range(n):
        x = int(input())
        if miller_rabin(x):
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    main()
