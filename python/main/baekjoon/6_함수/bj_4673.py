# https://www.acmicpc.net/problem/4673

def self_number(a: int):
    old_list = set(range(1, a + 1))
    add_list = set()

    for i in old_list:
        # 숫자 자리별 더하기, sum(map(int, "123")) -> 1+2+3 = 6
        test = i + sum(map(int, str(i)))
        add_list.add(test)

    # 정렬: sorted(set(), reverse=True)
    result = sorted(old_list - add_list)

    for x in result:
        print(x)

self_number(10000)

# 생성자, 셀프넘버
# d(n) 일때 n -> 생성자
# d(75) = 75+7+5 = 87 ,, 87의 생성자는 75
# d(87) = 87+8+7 = 102
# 101의 생성자
#     91: 91+9+1
#     100: 100+1+0+0
