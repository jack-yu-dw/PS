# p.321 럭키 스트레이트

n = input()
length = len(n)

sum1 = 0
sum2 = 0
for i in range(int(length/2)):
    sum1 += int(n[i])
for i in range(int(length/2), length):
    sum2 += int(n[i])

if sum1 == sum2:
    print("LUCKY")
else:
    print("READY")