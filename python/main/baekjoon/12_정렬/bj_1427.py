

li = list(input())
print(''.join(sorted(li, reverse=True)))



# li = list('53432')
#
# sorted(li, reverse=True) # <- ['5', '4', '3', '3', '2']
# print('################')
# print(li.sort()) # <- 에러남, sorted(list)를 쓰자.
#
# sort()
# 기존의 리스트를 변경함, 리스트만 이용가능
# sorted()
# 정렬값을 리턴함, 리스트 아니라도 사용 가능.


######################
# 첫번째로 푼 방식

# li = list(map(int, list(input())))
# li.sort(reverse=True)
#
# for i in li:
#     print(i, end='')


# https://www.acmicpc.net/problem/1427

# 배열을 정렬하는 것은 쉽다. 수가 주어지면, 그 수의 각 자리수를 내림차순으로 정렬해보자.
# 첫째 줄에 자리수를 내림차순으로 정렬한 수를 출력한다.

# 2143 -> 4321
# 500613009 -> 965310000
