k = int(input())

x, y = 1, 0

for _ in range(k):
    x, y = y, x + y

print(x, y)