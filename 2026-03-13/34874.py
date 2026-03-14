import sys

input = sys.stdin.readline

N, M = map(int, input().split())
scores = [list(map(int, input().split())) for _ in range(N)]

person_max = [max(row) for row in scores]

answer = []
for restaurant in range(M):
    cnt = 0
    for person in range(N):
        if scores[person][restaurant] < person_max[person]:
            cnt += 1
    answer.append(cnt)

print(*answer)