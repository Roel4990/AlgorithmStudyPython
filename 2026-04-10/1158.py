import sys
from collections import deque
input = sys.stdin.readline

N, K =map(int, input().split())

numbers = deque([i for i in range(1, N+1)])

removeList = []

while numbers:
    numbers.rotate(-K+1)
    removeList.append(numbers.popleft())

print("<" +", ".join(map(str, removeList))+">")