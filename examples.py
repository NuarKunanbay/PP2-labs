#1
print("Hello, World!")

#2
if 5 > 2:
  print("Five is greater than two!")

#3
if 5 > 2:
 print("Five is greater than two!") 
if 5 > 2:
        print("Five is greater than two!") 

#4
x = 5
y = "Hello, World!"

#5
#This is a comment.
print("Hello, World!")

#6
print("Hello, World!") #This is a comment

#7
#print("Hello, World!")
print("Cheers, Mate!")

#8
#This is a comment
#written in
#more than just one line
print("Hello, World!")

#9
"""
This is a comment
written in
more than just one line
"""
print("Hello, World!")

#10
x = 5
y = "John"
print(x)
print(y)

#11
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

#12
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

#13
x = 5
y = "John"
print(type(x))
print(type(y))

#14
x = "John"
# is the same as
x = 'John'

#15
a = 4
A = "Sally"
#A will not overwrite a

#16
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#17
myVariableName = "John"
MyVariableName = "John"
my_variable_name = "John"

#18
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#19
x = y = z = "Orange"
print(x)
print(y)
print(z)

#20
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#21
x = "Python is awesome"
print(x)

#22
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

#23
x = 5
y = 10
print(x + y)
x = 5
y = "John"
print(x, y)

#24
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

#25
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

#26
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

#27
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

#28
x = 5
print(type(x))

#29
x = 1    # int
y = 2.8  # float
z = 1j   # complex
print(type(x))
print(type(y))
print(type(z))

#30
x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))

#31
x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))

#32
x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))

#33
x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

#34
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

#35
import random

print(random.randrange(1, 10))

#36
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

#37
x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

#38
x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'

#39
print("Hello")
print('Hello')

#40
a = "Hello"
print(a)

#41
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

#42
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

#43
a = "Hello, World!"
print(a[1])

#44
for x in "banana":
  print(x)

#45
a = "Hello, World!"
print(len(a))

#46
txt = "The best things in life are free!"
print("free" in txt)

#47
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

#48
txt = "The best things in life are free!"
print("expensive" not in txt)

#49
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

#50 Slicing
b = "Hello, World!"
print(b[2:5])

#51
b = "Hello, World!"
print(b[:5])

#52
b = "Hello, World!"
print(b[2:])

#53
b = "Hello, World!"
print(b[-5:-2])

#54 Modify Strings
a = "Hello, World!"
print(a.upper())

#55
a = "Hello, World!"
print(a.lower())

#56
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

#57
a = "Hello, World!"
print(a.replace("H", "J"))

#58
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

#59 String Concatenation
a = "Hello"
b = "World"
c = a + b
print(c)

#60
a = "Hello"
b = "World"
c = a + " " + b
print(c)

#61 Format - Strings
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

#62
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

#63
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

#64 Escape Characters
txt = "We are the so-called \"Vikings\" from the north."
