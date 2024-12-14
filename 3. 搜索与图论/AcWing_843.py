def n_queens(n: int) -> None:
    board = [['.' for _ in range(n)] for _ in range(n)]
    col = [False] * n
    diag1 = [False] * (2 * n)
    diag2 = [False] * (2 * n)

    def dfs(row: int):
        if row == n:
            for line in board:
                print(''.join(line))
            print()
            return
        
        for i in range(n):
            if not col[i] and not diag1[row - i + n] and not diag2[row + i]:
                board[row][i] = 'Q'
                col[i] = diag1[row - i + n] = diag2[row + i] = True
                dfs(row + 1)
                board[row][i] = '.'
                col[i] = diag1[row - i + n] = diag2[row + i] = False
    
    dfs(0)


if __name__ == "__main__":
    n = int(input())
    n_queens(n)
