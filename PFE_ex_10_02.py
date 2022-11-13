import re
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
text = open(name)

maxauthor = dict()                                              #create a dictionary
timeSent = dict()                                               #create a list
#bits = list()

for line in text:
    line.rstrip()
    if not line.startswith("From "): continue                   #select lines that start with from
    words = line.split()
    hr = words[5].split(":")                                    #select the 5th index and split
    timeSent[hr[0]] = timeSent.get(hr[0],0) +1                  #idiom: retrieve/create/update counter

lst= list()                                                     #list creation for output
for k,v in timeSent.items():
    newtup = (k,v)                                              #variable to store inverted k,v
    lst.append((k,v))                                           #append tuples to list
    print("list",lst)
lst.sort()                                                      #sorting list by key

for k,v in lst:
    print(k,v)


    #     print(timeSent)
    # print("words",words)
    # for word in words:
    #     maxauthor[words[5]] = maxauthor.get(words[5],0)+1
    # print("max",maxauthor)

    # lst = list()
    # for key in maxauthor.items():
    #     newtup = maxauthor.keys()
    #     timeSent = newtup
    #
    # for lines in newtup:
    #     bits = lines.split()
    #     print(type(bits))
    #     print("list", bits)
    #     print("newtup", newtup)
    #     print("timeSent", timeSent)

#     for lines in maxauthor:
#         bits = lines.split()
#         timeSent[bits[0]] = timeSent.get(bits[0],0)+1
#     #print("words",words[5])
#         print("bits",bits[0])
#         print("TimeSent", timeSent)
#
#     print("max",maxauthor)
#
# largest = None
# largest_author = None
#
# for key in timeSent:
#     if largest is None: largest = timeSent[key]
#
#     if largest < timeSent[key]:
#         largest = timeSent[key]
#         largest_author = key
#
# print(largest_author, largest)