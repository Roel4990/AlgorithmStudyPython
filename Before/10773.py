import sys
input = sys.stdin.readline

t = int(input())
stack = []

for _ in range(t):
    num = int(input())
    if num == 0 :
        stack.pop()
    else :
        stack.append(num)

print(sum(stack))