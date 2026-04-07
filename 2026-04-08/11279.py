import sys
import heapq
input = sys.stdin.readline

heap = []
N = int(input())
for _ in range(N):
    n = int(input())
    if n != 0:
        heapq.heappush(heap, -n)
    else:
        if heap:
            print(-heapq.heappop(heap))
        else:
            print(0)