import sys
input = sys.stdin.readline

t = int(input())
stack = []

for _ in range(t):
    command = input().rstrip()
    # command.length 가 1 이상인 경우가 앞자리가 1인 경우
    if len(command) > 2:
        stack.append(int(command[2:]))
    # 2 인 경우 stack 에 값이 있으면 pop() 없으면 -1 출력
    elif command == '2':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif command == '3':
        print(len(stack))
    elif command == '4':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif command == '5':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])



