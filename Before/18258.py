import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
queue = deque([])
for i in range(n):
    list = input().rstrip().split()
    if len(list) == 2 :
        # push
        queue.append(list[1])
    else :
        if list[0] == "pop" :
            if len(queue) == 0:
                print(-1)
            else:
                print(queue.popleft())
        elif list[0] == "size":
            print(len(queue))
        elif list[0] == "empty":
            if len(queue) == 0:
                print(1)
            else:
                print(0)
        elif list[0] == "front":
            if len(queue) == 0:
                print(-1)
            else:
                print(queue[0])
        elif list[0] == "back":
            if len(queue) == 0:
                print(-1)
            else:
                print(queue[-1])