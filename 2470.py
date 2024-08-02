import sys

input = sys.stdin.readline

n = int(input())

numList = list(map(int, input().split()))

numList.sort()

# 투 포인터 정의
a, b = 0, n-1
# 0 에 가장 가까운 수
diff = abs(numList[a] + numList[b])
result = [numList[a], numList[b]]
while a < b:
    if abs(numList[a] + numList[b]) < diff:
        diff = abs(numList[a] + numList[b])
        result = [numList[a], numList[b]]
        if diff == 0:
            break
    if numList[a] + numList[b] < 0:
        a += 1
    else:
        b -= 1
print(result[0], result[1])
