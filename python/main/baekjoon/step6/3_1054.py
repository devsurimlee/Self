# https://www.acmicpc.net/problem/1065


def sequence(a: int):

    # 100 미만이면 해당 값 리턴
    if a < 100: return print(a)

    before_list = range(100, a+1)
    cnt = 99

    # 100이상일시 for문 돌림
    for num in before_list:
        # 해당값 분해 예) 100 -> ['1', '0', '0']
        split_num = list(str(num))

        before = int(split_num[0])          # 1
        now = int(split_num[1])             # 0
        gap = before - now                # 1-0 = 1

        # 3번째 자리부터 시작
        for i in range(2, len(split_num)):
            before = int(split_num[i-1])
            now = int(split_num[i])

            # 이전 gap과 다를 경우 다음 숫자로 넘어감
            if gap != (before - now):
                break
            if i == len(split_num)-1:
                cnt += 1
    print(cnt)

sequence(int(input()))

