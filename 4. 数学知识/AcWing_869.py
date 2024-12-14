from typing import List

def divide(x: int) -> List[int]:
    ans = []
    for i in range(1, int(x**0.5) + 1):
        if x % i == 0:
            ans.append(i)
            if i != x // i:
                ans.append(x // i)
                
    return sorted(ans)


def main():
    n = int(input())
    while n > 0:
        n -= 1
        x = int(input())
        res = divide(x)
        print(" ".join(map(str, res)))


if __name__ == "__main__":
    main()
