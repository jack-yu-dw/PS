# p.96 숫자 카드 게임
n, m = map(int, input().split())

candidate = []
for _ in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    candidate.append(min_value)

result = max(candidate)
print(result)