import sys
input = sys.stdin.readline

N, L = map(int, input().split())

for i in range(L, 101):
    value = N - (i**2-i) // 2
    if value < 0:
        print(-1)
        break
    if value % i == 0:
        value //= i
        print(*[value+j for j in range(i)])
        break
else:
    print(-1)