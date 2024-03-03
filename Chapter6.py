# lists
fruits = ["peaches", "pears", "apples"]
years = [3, "1998", 2.5, 987, "1994"]

# Check memnber in list & count
print ("apple" in fruits)
print ("apples" in fruits)
print(fruits.count("apples"))

#Check index of apples
print (fruits.index("apples"))


print(fruits, years)

# add item to list
fruits.append("oranges")
print(fruits)

# add list in years to fruits
fruits.extend(years)
print(fruits)

# remove item from list
fruits.remove("oranges")
print(fruits)

# remove item by Sequence from 1st of  list
fruits.pop(0)
print(fruits)

# remove item by Sequence from last of list
fruits.pop(-1)
print(fruits)

# sort number asc
numbers = [55, 20, 350, 99, 345, 78, 84, 37, 405]
numbers.sort
print(numbers) 
