#https://www.acmicpc.net/problem/1110

n = int(input())

if (n<10):
    n *= 10;

tens = n // 10
ones = n % 10
new_n = (ones * 10) + ((tens+ones) % 10)

i = 1
while (new_n != n):
    tens = new_n // 10
    ones = new_n % 10
    new_n = (ones*10) + ((tens+ones)%10)
    i += 1

print(i)