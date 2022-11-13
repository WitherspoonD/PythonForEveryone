# Use words.txt as the file name
fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print('File cannot be opened:', fname)
    quit()

count = 0
#y = fh.read()
for x in fh:
    x = x.rstrip()
    #if "NEW" in x:
    count = count + 1
    #y = int(x)
    #y = y + 1
    print(x)
print('Line Count: ', count)