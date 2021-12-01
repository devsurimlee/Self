# https://www.acmicpc.net/problem/4673


def self_number(a: int):
    old_list = set(range(1, a + 1))
    add_list = set()

    for i in old_list:
        test = i + sum(map(int, str(i)))
        add_list.add(test)
        add_list - old_list

    result = list(old_list - add_list)

    print(result)

self_number(100)

# 생성자, 셀프넘버
# d(n) 일때 n -> 생성자
# d(75) = 75+7+5 = 87 ,, 87의 생성자는 75
# d(87) = 87+8+7 = 102
# 101의 생성자
#     91: 91+9+1
#     100: 100+1+0+0
