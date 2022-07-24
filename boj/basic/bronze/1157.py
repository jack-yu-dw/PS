# https://www.acmicpc.net/problem/1157
# 참고) https://codechacha.com/ko/python-initialize-dict/#2-dict로-딕셔너리-초기화
# 참고) https://codechacha.com/ko/python-sorting-dict/#value를-기준으로-정렬-내림차순
# 참고) https://yang-wistory1009.tistory.com/38
# 참고) https://www.delftstack.com/ko/howto/python/get-first-key-in-dictionary-python/

str = input()
str = str.upper()

data = dict()
for i in str:
    if i in data:
        data[i] += 1
    else:
        data[i] = 1

# sorted_data 는 key-value 값을 tuple 형태의 원소로 갖는 list 가 된다!
sorted_data = sorted(data.items(), key=lambda item: item[1], reverse=True)

if len(sorted_data) != 1:
    if sorted_data[0][1] == sorted_data[1][1]:
        print('?')
    else:
        print(sorted_data[0][0])
else:
    print(sorted_data[0][0])
