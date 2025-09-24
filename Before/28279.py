import sys

from collections import deque

input = sys.stdin.readline

n = int(input())

queue = deque([])

for _ in range(n):
    temp = list(map(int, input().split()))
    if len(temp) == 2:
        if temp[0] == 1:
            queue.appendleft(temp[1])
        else :
            queue.append(temp[1])
    else:
        if temp[0] == 3:
            if len(queue) == 0:
                print(-1)
            else:
                print(queue.popleft())
        elif temp[0] == 4:
            if len(queue) == 0:
                print(-1)
            else:
                print(queue.pop())
        elif temp[0] == 5:
            print(len(queue))
        elif temp[0] == 6:
            if len(queue) == 0:
                print(1)
            else:
                print(0)
        elif temp[0] == 7:
            if len(queue) == 0:
                print(-1)
            else:
                print(queue[0])
        elif temp[0] == 8:
            if len(queue) == 0:
                print(-1)
            else:
                print(queue[-1])

