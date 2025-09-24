def dfs(row, cols, diag1, diag2):
    global n
    # 모든 행을 배치한 경우 -> 해답 1개 완성
    if row == n:
        return 1

    count = 0
    available = ((1 << n) - 1) & ~(cols | diag1 | diag2)
    while available:
        col = available & -available  # 가장 오른쪽 1비트 선택
        available -= col
        count += dfs(
            row + 1,
            cols | col,
            (diag1 | col) << 1,
            (diag2 | col) >> 1
        )
    return count

n = int(input().strip())
print(dfs(0, 0, 0, 0))
