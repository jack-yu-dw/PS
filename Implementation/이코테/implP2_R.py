# p.322 문자열 재정렬 (다시 풀어보기 : isalpha(), join())

s = input()

alphabet = []
sum = 0
for i in s:
    if i.isalpha():
        alphabet.append(i)
    else:
        sum += int(i)

alphabet.sort()
if sum != 0:
    alphabet.append(str(sum))

print(''.join(alphabet))