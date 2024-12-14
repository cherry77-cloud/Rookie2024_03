import sys
from typing import List, Union

def linear_gaussian_elimination(matrix: List[List[float]], epsilon=1e-6) -> Union[List[float], str]:
    n, m = len(matrix), len(matrix[0]) - 1
    col = row = 0
    for col in range(m):
        pivot = max(range(row, n), key=lambda i: abs(matrix[i][col]))
        if abs(matrix[pivot][col]) < epsilon:
            continue
        matrix[row], matrix[pivot] = matrix[pivot], matrix[row]
        for i in range(row + 1, n):
            factor = matrix[i][col] / matrix[row][col]
            for j in range(col, m + 1):
                matrix[i][j] -= factor * matrix[row][j]
        
        row += 1
        if row == n:
            break
    
    if any(abs(matrix[i][m]) > epsilon for i in range(row, n)):
        return "No solution"
    
    if row < m:
        return "Infinite group solutions"
    
    solution = [0.0] * m
    for i in range(row - 1, -1, -1):
        solution[i] = (matrix[i][m] - sum(matrix[i][j] * solution[j] for j in range(i + 1, m))) / matrix[i][i]
    return solution


def main():
    n = int(sys.stdin.readline())
    matrix = [list(map(float, sys.stdin.readline().split())) for _ in range(n)]
    result = linear_gaussian_elimination(matrix)
    if isinstance(result, list):
        for x in result:
            print(f"{x:.2f}")
    else:
        print(result)


if __name__ == "__main__":
    main()
