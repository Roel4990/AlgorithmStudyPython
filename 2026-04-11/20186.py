import sys

input = sys.stdin.readline
n, k = map(int, input().split())

numbers = list(map(int, input().split()))

numbers.sort(reverse=True)

sumValue = 0
for i in range(k):
    sumValue += numbers[i] - i

print(sumValue)