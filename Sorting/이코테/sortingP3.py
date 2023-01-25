# p.361 실패율
# https://school.programmers.co.kr/learn/courses/30/lessons/42889

def solution(N, stages):
    current = [0]*(N+1) # 1단계~N단계에 멈춰있는 사람들 + 모두 클리어해서 N+1 인 사람들 (0에 위치)
    for stage in stages:
        if stage == N+1:
            current[0] += 1
        else:
            current[stage] += 1
    
    failure = []
    valid_member = len(stages)
    for i in range(1, len(current)):
        if valid_member != 0:
            fail_rate = current[i] / valid_member
            failure.append((fail_rate, i)) # (실패율, 스테이지)
            valid_member -= current[i]
        else:
            failure.append((0, i))
    
    failure.sort(key = lambda x: (-x[0], x[1]))
    answer = []
    for f in failure:
        answer.append(f[1])
    return answer