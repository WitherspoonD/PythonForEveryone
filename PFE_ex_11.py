import re
fname = input("Enter file name: ")
if len(fname) < 1 : fname = "regex_sum1670906.txt"
handler = open(fname)

sum = 0
for items in handler:
    rstrip = items.rstrip()
    num = re.findall("[0-9]+", rstrip)
    for values in num:
        strToInt = int(values)
        sum = sum + strToInt
print(sum)