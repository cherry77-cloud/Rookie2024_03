def quick_power_mod(base: int, exponent: int, modulus: int) -> int:
    result = 1
    base = base % modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result


if __name__ == "__main__":
    n = int(input())
    for _ in range(n):
        a, b, c = map(int, input().split())
        result = quick_power_mod(a, b, c)
        print(result)
