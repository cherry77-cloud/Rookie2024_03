def newton_root(x: float) -> float:
    if x == 0: return 0
    C = x
    x0 = x
    EPS = 1e-8
    while True:
        xi = (2 * x0 * x0 * x0 + C) / (3 * x0 * x0)
        if abs(xi - x0) < EPS:
            break
        x0 = xi
    return x0


if __name__ == "__main__":
    x = float(input())
    ans = newton_root(x)
    print(f"{ans:.6f}")
