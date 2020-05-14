
H, M = input().split()

M = int(M)
H = int(H)


if M < 45:
    H = H-1
    if H < 0:
        H = 23
    M = M-45+60
else:
    M = M-45

print(H, M)
