from itertools import product
from string import ascii_lowercase

words = [''.join(i) for i in product(ascii_lowercase, repeat=3)]


words_name = 0
short_list = []
for i in words:
    if i[0] in "e" and i[2] in "aeiou" and i[1] not in "aeiou":
        words_name += 1
        short_list.append(i)

print(short_list)
print("Your name is esi")
print("Word Count is " + str(words_name))
