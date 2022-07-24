# https://www.acmicpc.net/problem/2941

word = input()

# c= , c- , dz= , d- , lj , nj , s= , z=
alphabet = 0
for i in range(len(word)):
    if i <= len(word)-2:
        if word[i] == 'c':
            if word[i+1] == '=' or word[i+1] == '-':
                continue
            else:
                alphabet += 1
        elif word[i] == 'd':
            if i < len(word)-2:
                if (word[i+1] == 'z' and word[i+2] == '=') or (word[i+1] == '-'):
                    continue
                else:
                    alphabet += 1
            else:
                if word[i+1] == '-':
                    continue
                else:
                    alphabet += 1
        elif word[i] == 'l' or word[i] == 'n':
            if word[i+1] == 'j':
                continue
            else:
                alphabet += 1
        elif word[i] == 's':
            if word[i+1] == '=':
                continue
            else:
                alphabet += 1
        elif word[i] == 'z':
            if word[i+1] == '=':
                continue
            else:
                alphabet += 1
        elif word[i] == '=' or '-':
            alphabet += 1
        else:
            alphabet += 1
    else: # if i = len(word)-1
        alphabet += 1

print(alphabet)