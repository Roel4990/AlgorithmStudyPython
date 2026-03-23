import sys

input = sys.stdin.readline
n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    if a == 1:
        print(1)
    else:
        restList = []
        checkNum = 1
        for i in range(10):
            checkNum *= a
            checkNum %= 10
            if checkNum in restList:
                break
            restList.append(checkNum)
        idx = b % len(restList)
        result = restList[idx-1]
        if result == 0:
            print(10)
        else:
            print(result)
