import sys
input=sys.stdin.readline

N = int(input())
persons = list(map(int, input().split()))

persons.sort()

num = 0
result = 0
for person in persons:
    num += person
    result += num
print(result)