# p.355 블록 이동하기 (풀이는 유사하게 고안했으나 구현 방식에서 틀림) (시간 초과)
# https://school.programmers.co.kr/learn/courses/30/lessons/60063

from collections import deque

def solution(board):
    partA = [0, 0] # 로봇의 왼쪽 파트
    partB = [0, 1] # 로봇의 오른쪽 파트
    count = 0
    cases = check_cases(board, partA, partB)
    q = deque()
    for case in cases:
        q.append((partA, partB, count, case))
    while q:
        partA, partB, count, case = q.popleft()
        if (partA[0]==len(board)-1 and partA[1]==len(board)-1) or (partB[0]==len(board)-1 and partB[1]==len(board)-1):
            return count
        else:
            npartA = [0, 0]
            npartB = [0, 0]
            if case == 1: # 로봇이 가로로 놓여있고 밑으로 그대로 이동할 수 있으며 partA 가 가로 중 왼쪽에 있을 때
                npartA[0] = partA[0] + 1
                npartB[0] = partB[0] + 1
            elif case == 2: # 로봇이 가로로 놓여있고 밑으로 그대로 이동할 수 있으며 partB 가 가로 중 왼쪽에 있을 때
                npartA[0] = partA[0] + 1
                npartB[0] = partB[0] + 1
            elif case == 3: # 로봇이 가로로 놓여있고 오른쪽으로 그대로 이동할 수 있으며 partA 가 가로 중 왼쪽에 있을 때
                npartA[1] = partA[1] + 1
                npartB[1] = partB[1] + 1
            elif case == 4: # 로봇이 가로로 놓여있고 오른쪽으로 그대로 이동할 수 있으며 partB 가 가로 중 왼쪽에 있을 때
                npartA[1] = partA[1] + 1
                npartB[1] = partB[1] + 1
            elif case == 5: # 로봇이 가로로 놓여있고 왼쪽을 축으로 90도 회전할 수 있으며 partA 가 가로 중 왼쪽에 있을 때
                npartB[0] = partA[0] + 1
                npartB[1] = partA[1]
            elif case == 6: # 로봇이 가로로 놓여있고 왼쪽을 축으로 90도 회전할 수 있으며 partB 가 가로 중 왼쪽에 있을 때
                npartA[0] = partB[0] + 1
                npartA[1] = partB[1]
            elif case == 7: # 로봇이 가로로 놓여있고 오른쪽을 축으로 90도 회전할 수 있으며 partA 가 가로 중 왼쪽에 있을 때
                npartA[0] = partB[0] + 1
                npartA[1] = partB[1]
            elif case == 8: # 로봇이 가로로 놓여있고 오른쪽을 축으로 90도 회전할 수 있으며 partB 가 가로 중 왼쪽에 있을 때
                npartB[0] = partA[0] + 1
                npartB[1] = partA[1]
            elif case == 9: # 로봇이 세로로 놓여있고 밑으로 그대로 이동할 수 있으며 partA 가 세로 중 아래에 있을 때
                npartB[0] = partA[0]
                npartA[0] = partA[0] + 1
            elif case == 10: # 로봇이 세로로 놓여있고 밑으로 그대로 이동할 수 있으며 partB 가 세로 중 아래에 있을 때
                npartA[0] = partB[0]
                npartB[0] = partB[0] + 1
            elif case == 11: # 로봇이 세로로 놓여있고 오른쪽으로 그대로 이동할 수 있으며 partA 가 세로 중 아래에 있을 때
                npartA[1] = partA[1] + 1
                npartB[1] = partB[1] + 1
            elif case == 12: # 로봇이 세로로 놓여있고 오른쪽으로 그대로 이동할 수 있으며 partB 가 세로 중 아래에 있을 때
                npartA[1] = partA[1] + 1
                npartB[1] = partB[1] + 1
            elif case == 13: # 로봇이 세로로 놓여있고 아래를 축으로 90도 회전할 수 있으며 partA 가 세로 중 아래에 있을 때
                npartB[0] = partA[0]
                npartB[1] = partA[1] + 1
            elif case == 14: # 로봇이 세로로 놓여있고 아래를 축으로 90도 회전할 수 있으며 partB 가 세로 중 아래에 있을 때
                npartA[0] = partB[0]
                npartA[1] = partB[1] + 1
            elif case == 15: # 로봇이 세로로 놓여있고 위를 축으로 90도 회전할 수 있으며 partA 가 세로 중 아래에 있을 때
                npartA[0] = partB[0]
                npartA[1] = partB[1] + 1
            else: # 로봇이 세로로 놓여있고 위를 축으로 90도 회전할 수 있으며 partB 가 세로 중 아래에 있을 때
                npartB[0] = partA[0]
                npartB[1] = partA[1] + 1
            
            count += 1
            cases = check_cases(board, npartA, npartB)
            for c in cases:
                q.append((npartA, npartB, count, c))
    
    return
               

def check_cases(board, partA, partB):
    cases = []
    # 로봇이 가로로 놓여있을 때
    if partA[0] == partB[0]:
        # 밑으로 그대로 이동할 수 있을 때 (1)
        if partA[1] < partB[1]: # partA 가 가로 중 왼쪽에 있을 때
            if board[partA[0]+1][partA[1]] == 0 and board[partB[0]+1][partB[1]] == 0:
                cases.append(1)
        else: # partB 가 가로 중 왼쪽에 있을 때
            if board[partB[0]+1][partB[1]] == 0 and board[partA[0]+1][partA[1]] == 0:
                cases.append(2)
        
        # 오른쪽으로 그대로 이동할 수 있을 때
        if partA[1] < partB[1]: # partA 가 가로 중 왼쪽에 있을 때
            if board[partB[0]][partB[1]+1] == 0:
                cases.append(3)
        else: # partB 가 가로 중 왼쪽에 있을 때
            if board[partA[0]][partA[1]+1] == 0:
                cases.append(4)

        # 왼쪽을 축으로 90도 회전할 수 있을 때
        if partA[1] < partB[1]: # partA 가 가로 중 왼쪽에 있을 때
            if board[partB[0]+1][partB[1]] == 0 and board[partA[0]+1][partA[1]] == 0:
                cases.append(5)
        else: # partB 가 가로 중 왼쪽에 있을 때
            if board[partA[0]+1][partA[1]] == 0 and board[partB[0]+1][partB[1]] == 0:
                cases.append(6)

        # 오른쪽을 축으로 90도 회전할 수 있을 때
        if partA[1] < partB[1]: # partA 가 가로 중 왼쪽에 있을 때
            if board[partA[0]+1][partA[1]] == 0 and board[partB[0]+1][partB[1]] == 0:
                cases.append(7)
        else: # partB 가 가로 중 왼쪽에 있을 때
            if board[partB[0]+1][partB[1]] == 0 and board[partA[0]+1][partA[1]] == 0:
                cases.append(8)

    # 로봇이 세로로 놓여있을 때
    else:
        # 밑으로 그대로 이동할 수 있을 때
        if partA[0] > partB[0]: # partA 가 세로 중 아래에 있을 때
            if board[partA[0]+1][partA[1]] == 0:
                cases.append(9)
        else: # partB 가 세로 중 아래에 있을 떄
            if board[partB[0]+1][partB[1]] == 0:
                cases.append(10)

        # 오른쪽으로 그대로 이동할 수 있을 때
        if partA[0] > partB[0]:
            if board[partA[0]][partA[1]+1] == 0 and board[partB[0]][partB[1]+1] == 0:
                cases.append(11)
        else:
            if board[partB[0]][partB[1]+1] == 0 and board[partA[0]][partA[1]+1] == 0:
                cases.append(12)

        # 아래를 축으로 90도 회전할 수 있을 때
        if partA[0] > partB[0]: # partA 가 세로 중 아래에 있을 때
            if board[partB[0]][partB[1]+1] == 0 and board[partA[0]][partA[1]+1] == 0:
                cases.append(13)
        else: # partB 가 세로 중 아래에 있을 떄
            if board[partA[0]][partA[1]+1] == 0 and board[partB[0]][partB[1]+1] == 0:
                cases.append(14)

        # 위를 축으로 90도 회전할 수 있을 때
        if partA[0] > partB[0]: # partA 가 세로 중 아래에 있을 때
            if board[partA[0]][partA[1]+1] == 0 and board[partB[0]][partB[1]+1] == 0:
                cases.append(15)
        else: # partB 가 세로 중 아래에 있을 떄
            if board[partB[0]][partB[1]+1] == 0 and board[partA[0]][partA[1]+1] == 0:
                cases.append(16)
    
    return cases

board = []
for _ in range(5):
    board.append(list(map(int, input().split())))

print(solution(board))