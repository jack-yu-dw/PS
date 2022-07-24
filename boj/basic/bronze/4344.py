# https://www.acmicpc.net/problem/4344
# 참고) https://tooo1.tistory.com/228

c = int(input())

for _ in range(c):
    data = list(map(int, input().split()))
    n = data[0]
    avg = (sum(data) - data[0])/n

    cnt = 0
    for i in range(1, len(data)):
        if data[i] > avg:
            cnt += 1

    result = cnt*100/n
    print(f"{result:.3f}%")