# A는 임대로,제산세,보혐료 급여 등 고정비용
# B는 노트북 한 대를 생산하는데에 드는 비용
# C는 노트북 가격


def func():
    a, b, c = map(int, input().split())
    n = 1
    if c <= ((a+b*n)/n):
        print(-1)
        return
    while c*n <= a+b*n:
        n = n+1

    print(n)


func()
