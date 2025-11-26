import sys
input = sys.stdin.readline

row = [[False]*10 for _ in range(9)]
col = [[False]*10 for _ in range(9)]
sq = [[False]*10 for _ in range(9)]

sudoku = [list(map(int, input().split())) for _ in range(9)]
blank = []

for i in range(9):
    for j in range(9):
        val = sudoku[i][j]
        if val == 0:
            blank.append((i, j))
        else:
            k = (i//3)*3 + j//3
            row[i][val] = True
            col[j][val] = True
            sq[k][val] = True

def dfs(idx):
    if idx == len(blank):
        for r in sudoku:
            print(*r)
        sys.exit(0)

    y, x = blank[idx]
    k = (y//3)*3 + x//3

    for num in range(1, 10):
        if not row[y][num] and not col[x][num] and not sq[k][num]:
            row[y][num] = col[x][num] = sq[k][num] = True
            sudoku[y][x] = num

            dfs(idx + 1)

            row[y][num] = col[x][num] = sq[k][num] = False
            sudoku[y][x] = 0

dfs(0)