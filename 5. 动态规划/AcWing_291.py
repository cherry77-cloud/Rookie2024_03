from typing import List


def count_tilings(n: int, m: int) -> int:
    def is_valid_state(state: int) -> bool:
        cnt = 0
        for j in range(n):
            if state & (1 << j):
                if cnt & 1:
                    return False
                cnt = 0
            else:
                cnt += 1
        return cnt & 1 == 0
        
    M = 1 << n
    valid = [False] * M
    state_transitions = [[] for _ in range(M)]
    dp = [[0] * M for _ in range(m + 1)]

    for i in range(M):
        valid[i] = is_valid_state(i)

    for i in range(M):
        for j in range(M):
            if (i & j) == 0 and valid[i | j]:
                state_transitions[i].append(j)

    dp[0][0] = 1

    for i in range(1, m + 1):
        for j in range(M):
            for k in state_transitions[j]:
                dp[i][j] += dp[i - 1][k]

    return dp[m][0]


if __name__ == "__main__":
    while True:
        n, m = map(int, input().split())
        if n == 0 and m == 0:
            break
        print(count_tilings(n, m))
