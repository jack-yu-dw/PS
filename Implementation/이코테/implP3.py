# p.323 문자열 압축
# https://school.programmers.co.kr/learn/courses/30/lessons/60057

def solution(s):
    length = len(s)
    array = []
    result = []

    for i in range(1, length+1):
        array.append([s[0:i], 1])
        for j in range(i, length, i):
            if j+i <= length -1 :
                piece = s[j:j+i]
                if piece == array[-1][0]:
                    array[-1][1] += 1
                else:
                    array.append([piece, 1])
            else:
                piece = s[j:length]
                if piece == array[-1][0]:
                    array[-1][1] += 1
                else:
                    array.append([piece, 1])

        compression = ""
        for i in array:
            if i[1] != 0:
                if i[1] == 1:
                    compression += i[0]
                else:
                    compression += (str(i[1]) + i[0])
        result.append(len(compression))
        array.clear()

    return min(result)