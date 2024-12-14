def compute_gcd_lcm(a: int, b: int) -> int:
    def euclidean_gcd(x: int, y: int) -> int:
        while y:
            x, y = y, x % y
        return x

    gcd = euclidean_gcd(a, b)
    lcm = a * b // gcd if gcd != 0 else 0
    return gcd, lcm


def main():
    n = int(input())
    for _ in range(n):
        x, y = map(int, input().split())
        gcd, lcm = compute_gcd_lcm(x, y)
        print(gcd)

if __name__ == "__main__":
    main()
