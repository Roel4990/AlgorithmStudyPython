import sys
input = sys.stdin.readline
n = int(input())
stack = list(map(int, input().split()))
saveStack = []
insertNum = 1
for i in stack:
	saveStack.append(i)
	while saveStack and saveStack[-1] == insertNum:
		saveStack.pop()
		insertNum += 1
	if len(saveStack) > 1 and saveStack[-1] > saveStack[-2]:
		print("Sad")
		sys.exit()
if saveStack:
	print("Sad")
else:
	print("Nice")
