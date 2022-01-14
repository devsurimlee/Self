# https://www.acmicpc.net/problem/10809

import string

word = input()
lists = list(string.ascii_lowercase) # 소문자배열 선언

for i in lists:
    print(word.find(i))

##########################
# 속도 개선

word = input()
lists = list(range(ord('a'), ord('z')+1))   # 아스키코드로 배열 선언

for i in lists:
    print(word.find(chr(i)))
    
# chr() 아스키코드 -> 문자

