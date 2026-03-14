n = int(input())

cnt = 0

while n>1:
    num = n//5
    cnt += num
    n = num
print(cnt)