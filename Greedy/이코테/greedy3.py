# p.99 1이 될 때까지
n, k = map(int, input().split())

count = 0

while True:
    if n == 1:
        break
    else:
        if n % k != 0:
            n -= 1
            count += 1
        else:
            n /= k
            count += 1

print(count)