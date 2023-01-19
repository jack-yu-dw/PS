# p.346 괄호 변환
# https://school.programmers.co.kr/learn/courses/30/lessons/60058

def solution(p):
    if p == '':
        return ''
    else:
        if check_pair(p):
            return p
        else:
            u, v = split(p)
            if check_pair(u):
                v = solution(v)
                return u + v
            else:
                answer = '('
                v = solution(v)
                answer += v + ')'
                u = u[1:-1]
                new_u = ''
                for i in u:
                    if i == '(':
                        new_u += ')'
                    else:
                        new_u += '('
                answer += new_u
                return answer


# "올바른 괄호 문자열" 인지 확인
def check_pair(w):
    if len(w) >= 2: # 유효한 입력일 때
        stack = []
        for i in range(len(w)):
            if len(stack) == 0: # 스택이 비어있을 때
                if w[i] == ')': # 현재 문자가 ')' 일 때
                    return False
                else: # 첫 문자가 '(' 일 때
                    stack.append(w[i]) # 현재 문자를 스택에 삽입
                
            else: # 스택이 비어있지 않을 때 ,,, 스택의 상단에는 항상 '(' 가 와있어야 한다 ... 그래야만이 올바른 괄호 문자열이므로
                if w[i] == '(':
                    stack.append(w[i])
                else:
                    stack.pop()
        
        if len(stack) == 0: # 만약 스택이 비어있다면
            return True
        else: # 만약 스택이 비어있지 않다면
            return False

    else: # 유효하지 않은 입력 (ex. "", "(", ")") 일 때
        return False

# 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리
def split(w):
    left = 0
    right = 0
    for i in range(len(w)):
        if w[i] == '(':
            left += 1
        else:
            right += 1 
        if left == right:
            if i == len(w)-1:
                u = w
                v = ''
            else:
                u = w[:i+1]
                v = w[i+1:]
            break
        
    return u, v
