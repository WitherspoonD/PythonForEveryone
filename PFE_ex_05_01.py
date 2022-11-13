# i = 0
# total = 0
# while True:
#     snum = input("Enter a number: ")
#     if snum == 'done':
#         break
#     try:
#         fnum = float(snum)
#     except:
#         print("invalid input")
#         continue
#     total = total + fnum
#  #   print(fnum)
#     i = i + 1
#
# #print('ALL DONE')
# print(total,i,total/i)

largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        inum = int(num)
    except:
        print("Invalid Input")
        continue
    if smallest is None:
        smallest = inum
    if largest is None or inum > largest:
        largest = inum
    elif inum < smallest:
        smallest = inum
    #print(num)

#print("Invalid Input")
print("Maximum", largest)
print("Minimum", smallest)
