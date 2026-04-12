import sys
input = sys.stdin.readline
n = int(input())
students = []
for i in range(n):
    c, s, score = map(int, input().split())
    students.append((score, c, s))
students.sort(reverse=True)
medal_count = {}

winners = []
for score, c, s in students:
    current_count = medal_count.get(c, 0)
    if current_count < 2:
        winners.append((c, s))
        medal_count[c] = current_count + 1
    if len(winners) == 3:
        break

for w in winners:
    print(w[0], w[1])
