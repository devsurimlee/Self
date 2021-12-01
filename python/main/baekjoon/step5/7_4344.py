# https://www.acmicpc.net/problem/4344

cnt = int(input())

for i in range(cnt):
    lists = list(map(int, input().split()))
    student = lists[0]
    avg = sum(lists[1:]) / student
    check = 0
    for x in lists[1:]:
        if x > avg: check += 1

    print('{:.3f}%'.format(check / student * 100))


# round(3.1234, 2)          -> 3.12
# {:.2f}.format(3.1234)     -> 3.12