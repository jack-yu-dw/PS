# p.115 왕실의 나이트
location = input()
row = int(location[1])
col = int(ord(location[0])) - int(ord('a')) + 1

possible_path = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]

result = 0

for path in possible_path:
    n_row = row + path[0]
    n_col = col + path[1]
    
    if n_row < 1 or n_col < 1 or n_row > 8 or n_col > 8:
        continue
    else:
        result += 1

print(result)
