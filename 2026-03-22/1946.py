import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    NList = []
    for _ in range(N):
        a, b  = map(int, input().split())
        # if b == 1:
        #     aFind = a
        NList.append((a, b))
    NList.sort(key=lambda x: (x[0]))
    cnt = 0
    value = N+1
    for i in range(N):
        if NList[i][1] < value:
            cnt += 1
            value = NList[i][1]
    print(cnt)



