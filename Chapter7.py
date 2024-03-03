# Dictionaries
stuff = {"food" : 15, "energy" : 100, "enemies" : 3}

# show value from key
#print(stuff.get("food"))

# show all key with value in dict
#print(stuff.items())

# show all key in dict
#print(stuff.keys())

# popitem is remove last key in dictionary
#print(stuff.popitem())
#print(stuff)


print(stuff.setdefault("food"))
print(stuff)
# add key and value to dictionary
print(stuff.setdefault("friends", 123))
print(stuff) 


new_items = {"rocks":4, "arrows": 18}
stuff.update(new_items)
print(stuff)

new_items = {"rocks": 2, "arrows": 5}
stuff.update(new_items)
print(stuff)

up_new = {"food": 3, "webs":2}
stuff.update(up_new)
print (stuff)

# Directly update
stuff.update(food = 450, cookie = 55)
print (stuff)