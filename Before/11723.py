import sys

input = sys.stdin.readline
S = set()
n = int(input())

for _ in range(n):
    list = input().strip().split()

    if len(list) == 1:
        if list[0] == "all":
            # 1 ~ 20인 집합으로 만들기
            S = set([i for i in range(1, 21)])
        else:
            # 공집합
            S = set()

    else:
        func, x = list[0], list[1]
        x = int(x)

        if func == "add":
            S.add(x)
        elif func == "remove":
            S.discard(x)
        elif func == "check":
            print(1 if x in S else 0)
        elif func == "toggle":
            if x in S:
                S.discard(x)
            else:
                S.add(x)