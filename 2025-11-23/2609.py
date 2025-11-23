import sys
input = sys.stdin.readline
a, b = map(int, input().split())
aCopy, bCopy = a, b

while bCopy != 0:
    aCopy, bCopy = bCopy, aCopy % bCopy

gcd = aCopy

lcm = a * b // gcd

print(gcd, lcm, sep="\n")