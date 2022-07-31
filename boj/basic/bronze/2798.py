# https://www.acmicpc.net/problem/2798

n, m = map(int, input().split())

card = list(map(int, input().split()))

max = 0
for i in range(len(card)-2):
    for j in range(i+1,len(card)-1):
        for k in range(j+1, len(card)):
            sum = card[i] + card[j] + card[k]
            if sum > max and sum <= m:
                max = sum

print(max)