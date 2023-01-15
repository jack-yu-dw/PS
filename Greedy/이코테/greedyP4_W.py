# p.314 만들 수 없는 금액 (풀이 고안 못함)

n = int(input())
coins = list(map(int, input().split()))
coins.sort()

target = 1

for coin in coins:
    if coin > target:
        break
    else:
        target += coin

print(target)