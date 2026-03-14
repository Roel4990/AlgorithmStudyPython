from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [list(map(int, ' '.join(input().split()))) for _ in range(N)]

queue = deque([(0, 0)])

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 1:
            graph[nx][ny] = graph[x][y] + 1
            queue.append((nx, ny))

print(graph[N - 1][M - 1])