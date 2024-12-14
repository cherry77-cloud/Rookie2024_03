from typing import List, Tuple

def prime_factors(x: int) -> List[Tuple[int, int]]:
    result = []
    factor = 2
    while factor * factor <= x:
        count = 0
        while x % factor == 0:
            x //= factor
            count += 1
        if count > 0:
            result.append((factor, count))
        factor += 1

    if x > 1:
        result.append((x, 1))

    return result


def main():
    n = int(input())
    for _ in range(n):
        x = int(input())
        factors = prime_factors(x)
        for factor, count in factors:
            print(f"{factor} {count}")
        print()

if __name__ == "__main__":
    main()
