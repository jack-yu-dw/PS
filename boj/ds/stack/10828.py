# https://www.acmicpc.net/problem/10828

import sys

n = int(input())
stack = []

for _ in range(n):
    line = sys.stdin.readline().split()
    if line[0] == 'push':
        stack.append(int(line[1]))
    elif line[0] == 'pop':
        if len(stack)!=0:
            print(stack.pop())
        else:
            print(-1)
    elif line[0] == 'size':
        print(len(stack))
    elif line[0] == 'empty':
        if len(stack)!=0:
            print(0)
        else:
            print(1)
    elif line[0] == 'top':
        if len(stack)!=0:
            print(stack[-1])
        else:
            print(-1)