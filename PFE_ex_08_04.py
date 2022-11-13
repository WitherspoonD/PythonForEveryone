fname = input("Enter file name: ")
#fh = open('romeo.txt')
fh = open(fname)
lst = list()
sentence = list()
for line in fh:
    line = line.rstrip()
    sentence = line.split()
    for words in sentence:
        if words not in lst:
            lst.append(words)
lst.sort()
print(lst)
