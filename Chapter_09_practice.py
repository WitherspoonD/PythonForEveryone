fileName = input("Enter the name of the file: ")
if len(fileName) < 1: fileName = "Customers.csv"
handler = open(fileName)
#print(handler)

mostSalesPerState = dict()
mostSalesPerZip = dict()

for line in handler:
    line.rstrip()
    words = line.split(",")
    bits = words[6]
    print(words)
    mostSalesPerState[words[6]] = mostSalesPerState.get(words[6],0) + 1
    mostSalesPerZip[words[7]] = mostSalesPerZip.get(words[7],0) + 1
    print("states",mostSalesPerState)                                      # states
    # print("bits------",bits)

mostSales = None
mostSalesz = None
zipSales = None
zipSalesz = None

lst= list()
for key, value in mostSalesPerState.items():
    newtup = (value,key)
    lst.append((key, value))
    print("newtup",newtup)
    #print("list",lst.sort())
    if mostSales is None: mostSales = mostSalesPerState[key]

    if mostSales < mostSalesPerState[key]:
        mostSales = mostSalesPerState[key]
        mostSalesz = key

# for key, value in lst:
#     print(key,value)


for count in mostSalesPerZip:
    print(mostSalesPerZip)
    newtup = (count)
    lst.append(count)

    if zipSales is None: zipSales = mostSalesPerZip[count]

    if zipSales < mostSalesPerZip[count]:
        zipSales = mostSalesPerZip[count]
        zipSalesz = count

print(mostSales,mostSalesz)
print(zipSales,zipSalesz)


