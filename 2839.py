N = int(input())
x = 0
y = 0
q = int((N / 5))


if N == 3:
    print(1)
elif N == 5:
    print(1)

else:
    if (N % 5) % 3 != 0:
        q = q-1
    while (N-(5*q)) % 3 != 0:
        q = q-1

    y = q
    x = int((N-5*y)/3)

    if x < 0 or y < 0:
        print(-1)

    else:
        print(x+y)
