N = int(input())
weights = list(map(int, input().split()))

weights.sort()

target = 0

for weight in weights:
    if weight > target + 1:
        break
    target += weight

print(target + 1)