# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
#error handling for mispelled filename
try:
    fh = open(fname)
except:
    print(f'File {fname} cannot be found, try again.')
    quit()
count = 0
total = 0
total2 = list()
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") is True:
        continue
    if line.startswith("X-DSPAM-Confidence:") is True:
        count = count + 1
        strcon = line.rstrip()
        atpos = strcon.find(':')
        host = line[atpos+1 : ]
        num = float(host)
        total = total + num
        # testing program using list functions. Adds num to list total2
        total2.append(num)
        #print(atpos , type(num))
    #print(line)
# print(count)
print(total2)
print(sum(total2))
print(len(total2))
print(total2.sort())
# print(host)
print("Average spam confidence:", total/count)
print("Average spam confidence:", sum(total2)/len(total2))
