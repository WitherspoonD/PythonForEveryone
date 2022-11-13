import re

fileName = input("Enter the name of the file: ")
if len(fileName) < 1: fileName = "mbox-short.txt"
handler = open(fileName)

email = dict()
sentence = list()

for line in handler:
    line = line.rstrip()
    sentence = line.split()
    for word in sentence:
        words = line.split()
        if not word.__contains__("@"):continue
        sentence = word.split()
        # print("found",words)
        #print("sentence",sentence)
        email[sentence[0]] = email.get(sentence[0],0) +1

# From chapter 11.2 // this works when the top part is commented out
numlist = list()
for line in handler:
    line = line.rstrip()
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
    if len(stuff) != 1 : continue
    num = float(stuff[0])
    numlist.append(num)
print("Maximum:", max(numlist))
# From Chapter 11.2 ^^^^^^^^^

largest = None
largest_author = None

for key in email:
    if largest is None: largest = email[key]

    if largest < email[key]:
        largest = email[key]
        largest_author = key
        #key2 = int(key)
    # for k,v in email:
    #     print("email", email)
tmp = list()
headers = ["Number", "Square", "Cube"]
#values = email.items()
for k,v in email.items():
    newtup = (v,k)
    tmp.append(newtup)

tmp = sorted(tmp, reverse=True)
#print(tmp)

for v,k in tmp[:10]:
    print(v,k)
    #print(email.items())
#
# row_format ="{:>10}" * (len(headers) + 1)
# print(row_format.format("", *headers))
#
# for value, row in zip(headers, values):
#     print(row_format.format("", row))


#print(largest_author[key2], largest[key2])
  # print("line",line)
    #wordy = words.split()
    #print("wordy",wordy)
    # if words.find('@'):
    #     print("true")
    #     continue
    #     wordy = line
    #     #print(line)
    #   #words = line.find('@')

