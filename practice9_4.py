fname = input("Enter file:")
if len(fname) < 1: fname = "mbox-short.txt"
handle = open(fname)

maxauthor = dict()

for eachLine in handle:
    eachLine.rstrip()
    if not eachLine.startswith("From "): continue
    words = eachLine.split()
    #print(words[1])
    maxauthor[words[1]] = maxauthor.get(words[1],0) +1

    #print("maxauthor: ", maxauthor)

largest = None
largest_author = None

for eachWord in maxauthor:
    if largest is None: largest = maxauthor[eachWord]
    #print(eachWord,largest)

    if largest < maxauthor[eachWord]:
        largest = maxauthor[eachWord]
        largest_author = eachWord
print(largest_author,largest)
    #if largest < maxauthor[eachWord]:
    #     largest = maxauthor.values()
    # print(largest)
# bigcount = None
# bigword = None
# for eachWord,y in maxauthor.items():
#     if bigcount is None or y > bigcount:
#         bigword = words
#         bigcount = y
# print("Big Count:" , bigcount, "Big Word: ", bigword)
