import sys
import json
input = sys.stdin.readline

json_string = '''{
    "]": "[",
    ")": "("
}'''
json_object = json.loads(json_string)

while True :
    str = input().rstrip()
    stack = []
    if str == ".":
        break
    for i in str:
        if i == '[' or i == '(':
            stack.append(i)
        elif i == ']':
            a = json_object[i]
            if len(stack) != 0 and stack[-1] == a:
                stack.pop()
            else:
                stack.append(')')
                break
        elif i == ')':
            a = json_object[i]
            if len(stack) != 0 and stack[-1] == a:
                stack.pop()
            else:
                stack.append(')')
                break
    if len(stack) == 0:
        print('yes')
    else:
        print('no')