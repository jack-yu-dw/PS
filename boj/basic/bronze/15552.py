# https://www.acmicpc.net/problem/15552
# 참고) https://home-body.tistory.com/299
# 참고) https://tooo1.tistory.com/310

import sys
t = int(input())

for i in range(t):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    print(a+b)


