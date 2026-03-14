from collections import Counter
import sys

input = sys.stdin.readline

N = int(input())
candies = list(map(int, input().split()))

count = Counter(candies)

if max(count.values()) <= 2:
    print("Yes")
else:
    print("No")