# p.316 무지의 먹방 라이브 (오답)

def solution(food_times, k):
    answer = 0
    i = 0
    n = 0
    while i != k:
        if food_times[n] != 0:
            food_times[n] -= 1
            n += 1
        else:
            n += 1
            if food_times[n] != 0:
                food_times[n] -= 1
                n += 1
        if n >= len(food_times):
            n = 0
        i += 1

    if len(set(food_times)) == 1 and 0 in set(food_times):
        answer = -1
    else:
        while food_times[n] == 0:
            n += 1
            if n >= len(food_times):
                n = 0
        answer = n+1
    return answer

food_times = [3, 2, 2, 2]
k = 8
print(solution(food_times, k))

'''
0-1: 2,2,2,2
1-2: 2,1,2,2
2-3: 2,1,1,2
3-4: 2,1,1,1
4-5: 1,1,1,1
5-6: 1,0,1,1
6-7: 1,0,0,1
7-8: 1,0,0,0
'''