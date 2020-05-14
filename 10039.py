s = []
result = 0

for i in range(5):
    tmp = int(input())
    if tmp < 40:
        tmp = 40
    s.append(tmp)
    result = result+s[i]


print((int(result/5)))
