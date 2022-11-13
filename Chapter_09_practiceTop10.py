fileName = input("Enter the name of the file: ")
if len(fileName) < 1: fileName = "Customers.csv"
handler = open(fileName)
#print(handler)

mostSalesPerState = dict()
mostSalesPerZip = dict()

for line in handler:
    line.rstrip()

    # split the sentence into words
    words = line.split(",")

    # grab 6th word in list and save to bits
    bits = words[6]

    # idiom: retrieve/create/update counter for each bit\/
    mostSalesPerState[bits] = mostSalesPerState.get(bits,0) + 1
    # print("states",mostSalesPerState)
    # print("bits------",bits)

lst = list()
for key, value in mostSalesPerState.items():

    # save the key value in value key order
    lst.append((value,key))
    #print("key",key)
    #print("list",lst.sort())

#sort list from highest to lowest
lst = sorted(lst, reverse=True)

#Print top 10 states by number of customers
for key, value in lst[:10]:
    #print(f'{value}\t\t{key}')
    print(f'{repr(key).rjust(4)} {repr(value).ljust(4)}')

