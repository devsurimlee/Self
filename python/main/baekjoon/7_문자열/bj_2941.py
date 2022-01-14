# https://www.acmicpc.net/problem/2941

# nljj

croatia_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
input_words = input()

for croatia in croatia_list:
    if croatia in input_words:
        input_words = input_words.replace(croatia, '*')

print(len(input_words))


# for croatia in croatia_list:
#     input_words = input_words.split(croatia)
#     print(input_words)

