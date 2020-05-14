
t = int(input())
num = input()

arr = []
sum = 0
for i in range(t):
    arr.append(num[i])
    sum = sum+int(arr[i])

print(sum)
