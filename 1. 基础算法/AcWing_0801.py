def hamming_weight(n: int) -> int:
    ret = 0
    while n:
        ret += 1
        n = n & (n - 1)
    return ret


if __name__ == "__main__":
    n = int(input())
    nums = [int(x) for x in input().split()]
    for num in nums:
        print(hamming_weight(num), end=" ")
