a = int(input())
test = []
x_cnt = 0
o_cnt = 0
for i in range(a):
    tmp = input()
    test.append(tmp)


for i in range(a):
    for j in range(len(test[i])):
        if test[i][j] == 'O':
            o_cnt = o_cnt+1
        elif test[i][j] == 'X'
