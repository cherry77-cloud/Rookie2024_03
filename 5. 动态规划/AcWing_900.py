def count_partitions1(n, mod=10**9+7):
    f = [[0] * (n + 1) for _ in range(n + 1)]
    f[1][1] = 1
    
    for i in range(2, n + 1):
        for j in range(1, i + 1):
            f[i][j] = (f[i - 1][j - 1] + f[i - j][j]) % mod
    
    result = 0
    for i in range(1, n + 1):
        result = (result + f[n][i]) % mod
    return result


def count_partitions2(n, mod=10**9+7):
    f = [0] * (n + 1)
    f[0] = 1
    
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            f[j] = (f[j] + f[j - i]) % mod
            
    return f[n]


if __name__ == "__main__":
    n = int(input())
    print(count_partitions1(n))
