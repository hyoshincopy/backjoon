h = []
b = []


for i in range(3):
    tmp = int(input())
    h.append(tmp)


for i in range(2):
    tmp = int(input())
    b.append(tmp)


print(min(h)+min(b)-50)
