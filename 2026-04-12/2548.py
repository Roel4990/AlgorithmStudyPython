import sys
input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))
nums.sort()
answer = nums[(n - 1) // 2]
print(answer)