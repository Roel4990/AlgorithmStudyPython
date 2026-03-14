n = int(input())
cnt = 0
for _ in range(n):
    a, b, c, d = map(int, input().split())
    if a >= 1000 or b >= 1600 or c >= 1500 or (0 < d <= 30):
        cnt += 1
print(cnt)