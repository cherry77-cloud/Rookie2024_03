def euler_phi(n: int) -> int:
    result = n
    i = 2
    while i * i <= n:
        if n % i == 0:
            while n % i == 0:
                n //= i
            result -= result // i
        i += 1
    if n > 1:
        result -= result // n
    return result


def main():
    n = int(input())
    for _ in range(n):
        x = int(input())
        print(euler_phi(x))


if __name__ == "__main__":
    main()
