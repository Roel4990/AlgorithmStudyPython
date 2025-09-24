import sys
input = sys.stdin.readline

def divideThree(str):
    num = len(str)
    if num == 1:
        return str
    else :
        return divideThree("-"*(num // 3)) + " "*(num // 3) + divideThree("-"*(num // 3))

while True:
    try:
        N = int(input())
        print(divideThree("-" * 3 ** N))
    except:
        break


