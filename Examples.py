# Removing elements from a dictionary

# create a dictionary
squares = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# remove a particular item, returns its value
# Output: 16
print(squares.pop(1))

# # Output: {1: 1, 2: 4, 3: 9, 5: 25}
# print(squares)
#
# # remove an arbitrary item, return (key,value)
# # Output: (5, 25)
# print(squares.popitem())
#
# # Output: {1: 1, 2: 4, 3: 9}
# print(squares)
#
# # remove all items
# squares.clear()
#
# # Output: {}
# print(squares)
#
# # delete the dictionary itself
# del squares
#
# # Throws Error
# print(squares)

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get("model"))
car["year"] = 2020
print(car["year"])

car["color"]="red"
print(car)

car.pop("model")
print(car)

car.clear()
print(car)