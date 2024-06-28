import sys

input = sys.stdin.readline
n = int(input())
numbers = sorted(list(map(int, input().split())))
a = int(input())

answer = 0
left, right = 0, n-1 # 왼쪽 오른쪽

while left < right:
    temp = numbers[left] + numbers[right]
    if temp == a:
        answer += 1
        left += 1
    elif temp < a:
        # 왼쪽 이동
        left += 1
    else:
        # 오른쪽 이동
        right -= 1

print(answer)