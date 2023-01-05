# p.92 큰 수의 법칙 ; 수열을 사용한 다른 풀이

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

result = 0

sequence = first*k + second
count = m // (k + 1)
left = m % (k + 1)

result = sequence * count + first * left
print(result)

# 책 풀이
# 가장 큰 수가 더해지는 횟수 계산
# count = int(m / (k + 1)) * k
# count += m % (k + 1)
# result += (count) * first # 가장 큰 수 더하기
# result += (m - count) * second # 두 번째로 큰 수 더하기
