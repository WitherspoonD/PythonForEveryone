fname = input('Enter File: ')
if len(fname) < 1: fname = 'mbox-short.txt'
file = open(fname)

maxAuthor = dict() # the author who sent the most emails
# data = dict() // not necessary
# emaildict = dict() // not necessary
for line in file:
    line.rstrip() # lin = lin.rstrip() not necessary to assign the line strip
    if not line.startswith("From "): continue
    words = line.split()
    maxAuthor
        #print(email)
    for x in maxAuthor:
        maxAuthor[x] = maxAuthor.get(x, 0) + 1
        print("email",maxAuthor)
    for w in words:
        #  the key is not there the count is zero
        #     oldcount = di.get(w,0)
        #     print(w,'old',oldcount)
        #     newcount = oldcount + 1
        #     di[w] = newcount\
        # Idiom: retrieve/create/update counter
        maxAuthor[w]= maxAuthor.get(w,0) + 1
        #print(w,'new', di[w])
    #print("di:",(di))

# now to find the most common word
largest = -1
theword = None
for k,v in maxAuthor.items():
    #print(k,v)
    if v > largest:
        largest = v
        theword = k
print('Done',theword,largest)
        # if w in di :
        #     di[w] = di[w] + 1
        # else:
        #     di[w] = 1
        #     print('##NEW##')
        # print(w,di[w])

# Use the file name mbox-short.txt as the file name
# fname = input("Enter file name: ")
# #error handling for mispelled filename
# try:
#     fh = open(fname)
# except:
#     print(f'File {fname} cannot be found, try again.')
#     quit()
# count_x = None
# count_y = None
# email = dict()
# for eachline in fh:
#     splitsentenceandstorewords = eachline.split()
#     for eachword in splitsentenceandstorewords:
#         if not eachline.startswith('From ')is True:
#             continue
#         if eachline.startswith('From ') is True:
#             email[eachword] = email.get(eachword,0) + 1
#             print(email.items())
#     #print(f'Words: {splitsentenceandstorewords}')
# totCount = None
# totWords = None
# for eachword, count in email.items():
#     if totCount is None or count > totCount:
#         totWords = eachword
#         totCount = count
# print(totWords,totCount)