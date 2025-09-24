import sys
input = sys.stdin.readline

n, price = map(int, input().split())
coins = []
for i in range(n):
    coins.append(int(input()))

coins.reverse()

cnt = 0

for coin in coins:
    if price ==0:
        break
    if coin <= price:
        a = price // coin
        cnt += a
        price -= a * coin
print(cnt)