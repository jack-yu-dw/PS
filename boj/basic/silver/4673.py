# https://www.acmicpc.net/problem/4673

def d(n):
    dn = n
    if dn >= 10:
        new_n = n
        while new_n // 10 > 0:
            dn += (new_n % 10)
            new_n = new_n // 10
        dn += new_n
    else:
        dn += n
    return dn

dn = []
for i in range(1, 10001):
    if d(i) not in dn and d(i) <= 10000:
        dn.append(d(i))

for i in range(1, 10001):
    if i not in dn:
        print(i)





