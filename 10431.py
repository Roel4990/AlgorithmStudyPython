import sys
input = sys.stdin.readline

def bubble_sort(arr):
    cnt = 0
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                cnt += 1
    return cnt
t = int(input())

for i in range(t):
    temp = list(map(int, input().split()))
    a, sorList = temp[0], temp[1:]
    print(a, bubble_sort(sorList))