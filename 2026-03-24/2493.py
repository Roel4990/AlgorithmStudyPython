import sys
input = sys.stdin.readline
n = int(input())
heights = list(map(int, input().split()))

stack = []
stack.append((sys.maxsize, 0))
result = []
for i in range(n):
    x = heights[i]
    while True:
        top_height, top_index = stack[-1]
        if top_height >= x:
            break
        stack.pop()
    result.append(top_index)
    stack.append((x, i + 1))

for num in result:
    print(num, end=' ')