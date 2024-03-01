# string data type

 # literal assignment
import math
first ="tarun"
last ="sharma"
 
# print(type( first))
# print(type( first) = str)
# print(isinstance(first,str))

 # constructor function
 # pizza = str("pepperoni")
 # print(type( pizza))
# print(type( pizza) = str)
# print(isinstance(pizza, str))

# concatenation
fullname = first + " " + last
print(fullname)

fullname += "!"
print(fullname)

# casting a number to a string
decade = str(1980)
print(type(decade))
print(decade)

statement = "I like rock music from the " + decade + "s."
print(statement)

# Multiple lines
multiline = '''
Hey, how are you?

I was just checking in.


'''
print(multiline)

# Escaping special characters
sentence = 'I\'m back at work!\tHey!\n\nWhere\'s this at\\located?'
print(sentence)

# String Methods

print(first)
print(first.lower())
print(first.upper())
print(first)

print(multiline.title())
print(multiline.replace("good", "ok"))
print(multiline)

print(len(multiline))
multiline += ""
multiline = ""
print(len(multiline))

print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))

print("")

# Build a menu
title = "menu".upper()
print(title.center(20, "="))
print("coffee".ljust(16, ".") + "$1".rjust(4))
print("Muffin". ljust(16, ".") + "$4".rjust(4))
print("cheesecake".ljust(16, ".") + "$4".rjust(4))

print("")

# string index values
print(first[1])
print(first[-1])
print(first[1:-1])
print(first[1:])

# some methods return boolean data
print(first.startswith("D"))
print(first.endswith("Z"))


# Boolean data type
myvalue = True
X = bool(False)
print(type(X))
print(isinstance(myvalue, bool))

# Numeric data types

# integer type
price = 100
best_price = int(80)
print (type(price))
print(isinstance(best_price,int))

# float type
gpa = 3.28
y = float(1.14)
print(type(gpa))

# complex type
comp_value = 5+3J
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

# Built-in functions for numbers

print(abs(gpa))
print(abs(gpa * -1))

print(round(gpa))

print(round(gpa, 1))

print (math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))

#casting a string to a number
Zipcode = "10001"
Zip_value = int(Zipcode)
print(type(Zip_value))

# Error if you attempt to cast incorrect data
# Zip_value = int("New York")



















 

