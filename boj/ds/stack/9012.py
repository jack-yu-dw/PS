# https://www.acmicpc.net/problem/9012

T = int(input())

for i in range(T):
    ps = list(input())
    while len(ps) != 0:
        if ps[0] == ')':
            print('NO')
            break
        else:
            if ')' in ps:
                ps.remove(')')
                ps.remove('(')
            else:
                print("NO")
                break
    if len(ps) == 0:
        print("YES")