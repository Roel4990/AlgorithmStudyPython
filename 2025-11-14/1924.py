import sys
input = sys.stdin.readline

mon, day = map(int, input().split()) # 월, 일

dayOfTheWeek = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
cnt = 0
dayList = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for i in range(mon-1):
    cnt +=  dayList[i]

cnt += day - 1

print(dayOfTheWeek[cnt%7])