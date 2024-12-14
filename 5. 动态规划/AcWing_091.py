from typing import List

def hamiltonian_circuit(n: int, weights: List[List[int]]) -> int:
    state_num = 1 << n
    f = [[float('inf')] * n for _ in range(state_num + 1)]
    f[1][0] = 0
    for i in range(state_num):
        for j in range(n):
            if (i >> j) & 1:
                for k in range(n):
                    if (i >> k) & 1 and k != j:
                        f[i][j] = min(f[i][j], f[i - (1 << j)][k] + weights[k][j])

    return f[(1 << n) - 1][n - 1]


if __name__ == "__main__":
    n = int(input())
    weights = []
    for _ in range(n):
        weights.append(list(map(int, input().split())))
    print(hamiltonian_circuit(n, weights))
