a, b = map(int, input().split())
nList = list(map(int, input().split()))

sumList = [0 for i in range(a-b+1)]
sumList[0] = sum(nList[0:b])

for i in range(len(nList)-b):
    sumValue = nList[i+b] - nList[i]
    sumList[i+1] = sumList[i] + sumValue

print(max(sumList))