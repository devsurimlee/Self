# https://www.acmicpc.net/problem/1157

# dictionary 사용

dics = {}
word = list(input().upper())

# 중복값 제외하고 for문 돌림
for x in set(word):
    dics[x] = word.count(x)

# value 값중 제일 큰 값
max_value = max(dics.values())

# max_value 개수 count해서 1개 일시 key값 print
cnt = list(dics.values()).count(max_value)
if cnt == 1:
    print(max(dics, key=dics.get))
elif cnt > 1:
    print("?")


#########################
# list 버전

lists = []
word = list(input().upper())
uniq_list = list(set(word))

for x in uniq_list:
    lists.append(word.count(x))

max_value = max(lists)
if lists.count(max_value) == 1:
    max_index = lists.index(max_value)
    print(uniq_list[max_index])
else:
    print('?')


#################################


# 시간초과 2

# dics = {}
# word = list(input().upper())
#
# for x in word:
#     dics[x] = word.count(x)
#
# max_value = max(dics.values())
# max_key = ''
#
# cnt = list(dics.values()).count(max_value)
# if cnt == 1:
#     print(max(dics, key=dics.get))
# elif cnt > 1:
#     print("?")


##############################
# 시간초과 1

# dics = {}
# word = list(input().upper())
#
# for x in word:
#     dics[x] = word.count(x)
#
# max_value = max(dics.values())
# max_key = ''
#
# for k, v in dics.items():
#     if v == max_value:
#         max_key += k
#
# if len(max_key) == 1:
#     print(max_key)
# else:
#     print('?')

#############################

# value 최고인 key 찾기, 해당 key가 여러개일 경우 앞선 순서 리턴함

# key = max(dics, key=dics.get)
# print(key)

# max_key = max(dics, key=lambda k: dics[k])
# print(max_key)


# 대문자변환 a.upper()
# 소문자 변환 A.lower()
