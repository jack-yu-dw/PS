# https://www.acmicpc.net/problem/8958
# 참고) https://choidr.tistory.com/entry/백준BOJ-Python-8958번

n = int(input())
for _ in range(n):
    test = input()

    result = 0
    for i in range(len(test)):
        if i == 0:
            if test[i] == 'O':
                cnt = 1
            else:
                cnt = 0
        else:
            if test[i] == 'O' and test[i-1] == 'O':
                cnt += 1
            elif test[i] == 'O' and test[i-1] != 'O':
                cnt = 1
            else:
                cnt = 0

        result += cnt

    print(result)