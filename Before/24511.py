import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

list_a = list(map(int, input().split()))
list_b = list(map(int, input().split()))

m = int(input())
list_c = list(map(int, input().split()))

result = deque()

for i in range(n):
    if list_a[i] == 0:
        result.appendleft(list_b[i])

for j in range(m):
    result.append(list_c[j])
    print(result.popleft(), end=' ')