import sys
input = sys.stdin.readline
N = int(input())
numbers = list(map(int, input().split()))

stack = []
result = [-1] * N
for i in range(N):
    while stack and numbers[stack[-1]] < numbers[i]:
        idx = stack.pop()
        result[idx] = numbers[i]
    stack.append(i)

print(*result)