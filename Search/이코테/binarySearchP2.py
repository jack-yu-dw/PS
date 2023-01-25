# p.368 고정점 찾기

n = int(input())
data = list(map(int, input().split()))

start = 0
end = n-1

while True:
    if start > end:
        print(-1)
        break
    mid = (start + end) // 2
    if data[mid] == mid:
        print(mid)
        break
    elif data[mid] > mid:
        end = mid - 1
    else:
        start = mid + 1