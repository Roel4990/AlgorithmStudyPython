import sys
input = sys.stdin.readline
from collections import Counter
N = int(input())
S = input()
counter = Counter(S)
print("Yes" if counter['O'] >= counter['X'] else "No")