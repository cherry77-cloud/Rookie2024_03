import sys
from typing import List, Union

def xor_gaussian_elimination(matrix: List[List[int]]) -> Union[List[int], str]:
    n = len(matrix)
    for i in range(n):
        if matrix[i][i] == 0:
            for j in range(i + 1, n):
                if matrix[j][i] == 1:
                    matrix[i], matrix[j] = matrix[j], matrix[i]
                    break
            else: continue
        for j in range(i + 1, n):
            if matrix[j][i] == 1:
                for k in range(i, n + 1): matrix[j][k] ^= matrix[i][k]
    
    for i in range(n - 1, -1, -1):
        if matrix[i][i] == 0:
            if matrix[i][n] == 1: return "No solution"
            continue
        for j in range(i): 
            if matrix[j][i] == 1: matrix[j][n] ^= matrix[i][n]
    
    if any(all(row[j] == 0 for j in range(i, n)) and row[n] == 0 for i, row in enumerate(matrix)):
        return "Multiple sets of solutions"
    
    return [row[n] for row in matrix]


def main():
    n = int(sys.stdin.readline())
    matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    result = xor_gaussian_elimination(matrix)
    if isinstance(result, list):
        for x in result: print(x)
    else:
        print(result)

if __name__ == "__main__":
    main()
