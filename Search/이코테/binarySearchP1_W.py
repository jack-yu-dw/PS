# p.367 정렬된 배열에서 특정 수의 개수 구하기 (유형 익히기)

from bisect import bisect_left, bisect_right # 중요!

n, x = map(int, input().split())
data = list(map(int, input().split()))
left = bisect_left(data, x)
right = bisect_right(data, x)
if right - left == 0:
    print(-1)
else:
    print(right - left)