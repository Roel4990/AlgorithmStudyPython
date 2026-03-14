import sys
input = sys.stdin.readline
n = int(input())

endPoint = 0
answer = 0

arr = []

for i in range(0,n):
    a, b = map(int, input().split())
    arr.append([a,b])

arr.sort(key=lambda x: (x[1], x[0]))
print(arr)
for newStart, newEnd in arr:
    if endPoint <= newStart:
        answer += 1
        endPoint = newEnd
print(answer)