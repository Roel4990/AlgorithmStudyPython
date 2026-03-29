import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    numbers = list(map(int, input().split()))
    num = 0
    for i in numbers:
        num += 1
        if num == i:
            num += 1
    print(num)