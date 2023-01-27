# p.370 가사 검색 (풀이 고안은 했으나 구현 부족) (효율성 테스트 통과 X)
# https://school.programmers.co.kr/learn/courses/30/lessons/60060

from bisect import bisect_left, bisect_right

# 값이 [left_value, right_value] 인 데이터의 개수를 반환하는 함수
def count_by_range(a, left_value, right_value):
    left_index = bisect_left(a, left_value)
    right_index = bisect_right(a, right_value)
    return right_index - left_index

# 모든 단어를 길이마다 나누어서 저장하기 위한 리스트
array = [[] for _ in range(10001)]
# 모든 단어를 길이마다 나누어서 뒤집어 저장하기 위한 리스트
reversed_array = [[] for _ in range(10001)]

def solution(words, queries):
    answer = []
    for word in words: # 모든 단어를 접미사 와일드카드 배열, 접두사 와일드카드 배열에 각각 삽입
        array[len(word)].append(word) # 단어를 삽입
        reversed_array[len(word)].append(word[::-1]) # 단어를 뒤집어서 삽입

    for i in range(10001): # 이진 탐색을 수행하기 위해 각 단어 리스트 정렬 수행
        array[i].sort()
        reversed_array[i].sort()

    for q in queries: # 쿼리를 하나씩 확인하며 처리
        if q[0] != '?': # 접미사에 와일드카드가 붙은 경우
            res = count_by_range(array[len(q)], q.replace('?', 'a'), q.replace('?', 'z'))
        else: # 접두사에 와일드카드가 붙은 경우
            res = count_by_range(reversed_array[len(q)], q[::-1].replace('?', 'a'), q[::-1].replace('?', 'z'))
        
        # 검색된 단어의 개수를 저장
        answer.append(res)
    return answer

'''
def solution(words, queries):
    answer = []
    for query in queries:
        si = 0
        ei = 0
        count = 0
        for t in range(len(query)):
            if count == 0 and query[t] == '?':
                si = t
                ei = t
                count += 1
            elif count != 0 and query[t] == '?':
                ei += 1
                count += 1
        if si == 0: # 키워드가 접두사 
            target_start = query[ei+1:]+'a'*count
            target_end = query[ei+1:]+'z'*count
            mode = 0 # 키워드가 접두사
        else: # 키워드가 접미사
            target_start = query[:si]+'a'*count
            target_end = query[:si]+'z'*count
            mode = 1 # 키워드가 접미사
        
        result = binary_search(words, query, target_start, target_end, si, ei, mode)
        answer.append(result)
        
    return answer

def binary_search(words, query, target_start, target_end, si, ei, mode):
    tmp = []
    for word in words:
        if len(word) == len(query):
            if mode == 0:
                tmp_word = word[ei+1:] + word[:ei+1]
                tmp.append(tmp_word)
            else:
                tmp.append(word)
    tmp.sort()
    left = bisect_left(tmp, target_start)
    right = bisect_right(tmp, target_end)
    return right - left


print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]))
'''