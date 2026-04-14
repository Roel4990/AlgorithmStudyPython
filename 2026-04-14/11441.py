import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
sumList = [0] * (N + 1)
sumList[1] = numbers[0]
for i in range(1, N+1):
    sumList[i] = sumList[i - 1] + numbers[i - 1]
for _ in range(int(input())):
    i, j = map(int, input().split())
    print(sumList[j] - sumList[i - 1])