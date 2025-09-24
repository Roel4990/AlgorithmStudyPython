import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
queue = deque(enumerate(map(int, input().split())))

while queue:
    a, b = queue.popleft()
    print(a + 1, end=' ')
    if b > 0:
        queue.rotate(-(b - 1))
    else:
        queue.rotate(-b)
