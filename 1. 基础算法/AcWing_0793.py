def multiply_high_precision(A: str, B: str) -> str:
    if B == '0' or A == '0':
        return '0'

    base_size = 9
    BASE = 10 ** base_size
    a_list = [int(A[max(i-base_size, 0):i]) for i in range(len(A), 0, -base_size)]
    b_list = [int(B[max(i-base_size, 0):i]) for i in range(len(B), 0, -base_size)]
    result = [0] * (len(a_list) + len(b_list))

    for i in range(len(a_list)):
        for j in range(len(b_list)):
            result[i + j] += a_list[i] * b_list[j]
            result[i + j + 1] += result[i + j] // BASE
            result[i + j] %= BASE

    for i in range(len(result) - 1):
        result[i + 1] += result[i] // BASE
        result[i] %= BASE

    while len(result) > 1 and result[-1] == 0:
        result.pop()

    return ''.join(str(x).zfill(9) for x in reversed(result)).lstrip('0')


if __name__ == "__main__":
    A = input().strip()
    B = input().strip()
    print(multiply_high_precision(A, B))
