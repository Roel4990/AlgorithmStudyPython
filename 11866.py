import sys
from collections import deque
input = sys.stdin.readline

n, b = map(int, input().split())
resList = []
queue = deque([i for i in range(1, n+1)])

while queue:
    queue.rotate(-(b-1))
    resList.append(queue.popleft())

print( "<" + ", ".join(map(str, resList)) + ">")