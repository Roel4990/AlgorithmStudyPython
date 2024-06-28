import sys
input = sys.stdin.readline


result = 0
def dfs(count):
    global result
    if count == N:
        result += 1
    for i in range(0, N):
        for j in range(0, N):
            if visited[i][j]:
                continue
            visited[i][j] = True
            for a in range(N):
                visited[i][a] = True  # 수평선
                visited[a][j] = True  # 수직선
            for a in range(N):
                if 0 <= i + a < N and 0 <= j + a < N:
                    visited[i + a][j + a] = True
                if 0 <= i - a < N and 0 <= j - a < N:
                    visited[i - a][j - a] = True
                    # 부 대각선
                if 0 <= i + a < N and 0 <= j - a < N:
                    visited[i + a][j - a] = True
                if 0 <= i - a < N and 0 <= j + a < N:
                    visited[i - a][j + a] = True

            dfs(count + 1)



N = int(input())
visited = [[False] * N for _ in range(N)]

dfs(1)

print(result)