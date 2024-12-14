from typing import List

def build_kmp_fail(pattern: str) -> List[int]:
    m = len(pattern)
    fail = [-1] * m
    for i in range(1, m):
        j = fail[i - 1]
        while j != -1 and pattern[j + 1] != pattern[i]:
            j = fail[j]
        if pattern[j + 1] == pattern[i]:
            fail[i] = j + 1
    return fail


def kmp_match(pattern: str, text: str) -> List[int]:
    n, m = len(text), len(pattern)
    fail = build_kmp_fail(pattern)
    matches = []
    j = -1
    for i in range(n):
        while j != -1 and pattern[j + 1] != text[i]:
            j = fail[j]
        if pattern[j + 1] == text[i]:
            j += 1
        if j == m - 1:
            matches.append(i - m + 1)
            j = fail[j]
    return matches


if __name__ == "__main__":
    n = int(input())
    s1 = input()
    m = int(input())
    s2 = input()
    result = kmp_match(s1, s2)
    print(" ".join(map(str, result)))
