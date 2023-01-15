# p.313 문자열 뒤집기

s = input()
zero = 0
one = 0
for i in range(len(s)-1):
    if s[i] == '0' and s[i+1] == '1':
        zero += 1
    elif s[i] == '1' and s[i+1] == '0':
        one += 1
    else: # (s[i] == '0' and s[i+1] == '0') or (s[i] == '1' and s[i+1] == '1')
        continue

if s[len(s)-1] == '0':
    zero += 1
else:
    one += 1

if zero > one:
    print(one)
else:
    print(zero)