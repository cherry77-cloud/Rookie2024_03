from typing import List, Tuple

def extended_chinese_remainder_theorem(m: List[int], a: List[int]) -> int:
    def extended_gcd(a: int, b: int) -> Tuple[int, int, int]:
        if b == 0:
            return a, 1, 0
        gcd, x, y = extended_gcd(b, a % b)
        return gcd, y, x - (a // b) * y

    def merge_equation(m1: int, r1: int, m2: int, r2: int) -> Tuple[int, int]:
        gcd, p, q = extended_gcd(m1, m2)
        if (r2 - r1) % gcd:
            return 0, 0
        lcm = m1 // gcd * m2
        r = (r1 + (r2 - r1) * p * (m1 // gcd)) % lcm
        return lcm, r

    lcm, r = m[0], a[0]
    for i in range(1, len(m)):
        lcm, r = merge_equation(lcm, r, m[i], a[i])
        if lcm == 0:
            return -1
    return r


def main():
    import sys
    n = int(sys.stdin.readline())
    m = []
    a = []
    for _ in range(n):
        mi, ai = map(int, sys.stdin.readline().split())
        m.append(mi)
        a.append(ai)

    result = extended_chinese_remainder_theorem(m, a)
    sys.stdout.write(str(result) + '\n')


if __name__ == "__main__":
    main()
