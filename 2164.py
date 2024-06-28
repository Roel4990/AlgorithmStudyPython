import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
queue = deque([i+1 for i in range(n)])

while True:
    queue.popleft()
    if len(queue) == 1:
        break
    queue.append(queue.popleft())

print(queue[0])