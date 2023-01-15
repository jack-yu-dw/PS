# p.315 볼링공 고르기 (다른 풀이 존재)

n, m = map(int, input().split())
data = list(map(int, input().split()))

count = 0
for i in range(n-1):
    for j in range(i+1, n):
        if data[i] != data[j]:
            count += 1

print(count)