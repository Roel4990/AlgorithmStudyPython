N = int(input())
data = list(map(int, input().split()))

ans = [0, 0]
cnt = [0, 0]

for a in data:
    t = a % 2
    cnt[t] += 1
    ans[t] += cnt[1 - t]

print(min(ans[0], ans[1]))