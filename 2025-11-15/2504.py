s = input().strip()
stack = []

for char in s:
    if char == '(' or char == '[':
        stack.append(char)
    else:
        temp = 0
        while stack:
            top = stack.pop()
            if top == '(' and char == ')':
                stack.append(2 if temp == 0 else 2*temp)
                break
            elif top == '[' and char == ']':
                stack.append(3 if temp == 0 else 3*temp)
                break
            elif isinstance(top, int):
                temp += top
            else:
                print(0)
                exit()
        else:
            print(0)
            exit()
result = 0
for x in stack:
    if not isinstance(x, int):
        print(0)
        exit()
    result += x

print(result)
