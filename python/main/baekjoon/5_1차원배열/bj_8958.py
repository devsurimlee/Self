# https://www.acmicpc.net/problem/8958

cnt = int(input())
result = 0;

for i in range(cnt):
    str = input()
    sum = 0
    check = 0
    for x in str:
        if x == 'O':
            check += 1
            sum += check
        else: check = 0
    print(sum)
