import sys
import math
input = sys.stdin.readline


i, j, a, b = list(map(int, input().split()))

print(math.ceil(j/(b+1))*math.ceil(i/(a+1)))