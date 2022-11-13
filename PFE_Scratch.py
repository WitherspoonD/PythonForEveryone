import re

file = open("regex_sum1670906.txt")

count = 0
tot = 0

import re
for line in file:
    rstrp = line.rstrip()
    num = re.findall('[0-9]+', rstrp)
    for values in num:
        str_to_int = int(values)
        count = count + 1
        tot = tot + str_to_int
#print(count, tot)
print(tot)
#Dictionaries
# store1=list()
# store2=list()
# prod=None
# defsolve(ar):\
#     store1=[2,4,5]
# for x in store1:
# ifprodisnotNone:
# prod=store1[x]
# print(store1)
#Writeyourcodehere
# name = input('Enter file:')
# handle = open(name)
#
# counts = dict()
# for line in handle:
#     words = line.split()
#     for word in words:
#        counts[word] = counts.get(word,0) + 1


# bigcount = None
# bigword = None
# for word, count in counts.items():
#     if bigcount is None or count > bigcount:
#         bigword = word
#         bigcount = count
#
# print(bigword, bigcount)
# purse = dict()
# purse['money'] = 12
# purse['candy'] = 3
# purse['tissues'] = 75
# print(f"This is a dictionary {purse}")
#
# counts = dict()
# names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
# for name in names:
#     counts[name] = counts.get(name, 0) + 1
# print(counts)

# stuff = list()
# stuff.append(input("Add something:"))
# stuff.append('99')
# print(stuff)
# some = [1,9,21,10,16]
# 9 in some
#How to use split()
# abc = 'With three words'
# stuff = abc.split()
# print(stuff)
# print(len(stuff))
# print(stuff[0])
# print(stuff)
# for w in stuff:
#     print(w)
# Lists part 3
# words2 = list()
# fhand = open('mbox-short.txt')
# for line in fhand:
#     line = line.rstrip()
#     if not line.startswith('From '):
#         continue
#     words = line.split()
#     words2 = line.split()
#     print("words", words)
#     email = words[1]
#     pieces = email.split('@')
# print(pieces[1])

# fruit = 'Banana'
# fruit[0] = 'b'
# print(fruit)
#
# name = input("Enter file:")
# if len(name) < 1 : name = "mbox-short.txt"
# text = open(name)
#
# maxauthor = dict()
#
# for line in text:
#     line.rstrip()
#     if not line.startswith("From "): continue
#     words = line.split()
#     maxauthor[words[1]] = maxauthor.get(words[1],0)+1
#
# largest = None
# largest_author = None
#
# for key in maxauthor:
#     if largest is None: largest = maxauthor[key]
#
#     if largest < maxauthor[key]:
#         largest = maxauthor[key]
#         largest_author = key
#
# print(largest_author, largest)