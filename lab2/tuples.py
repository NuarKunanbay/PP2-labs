#Examples
#1
mytuple = ("apple", "banana", "cherry")
#2
thistuple = ("apple", "banana", "cherry")
print(thistuple)
#3
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
#5
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))
#6
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))
#7
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
#8
tuple1 = ("abc", 34, True, 40, "male")
#9
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))
#10
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)
#11
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])
#12
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])
#13
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])
#14
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])
#15
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])
#16
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])
#17
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")
#18
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)
#19
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
#20
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)
#21
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
#22
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists
#Exercises
#1
fruits = ("apple", "banana", "cherry")
print(fruits[0])
#2
fruits = ("apple", "banana", "cherry")
print(len(fruits))
#3
fruits = ("apple", "banana", "cherry")
print(fruits[-1])
#4
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))
#5
fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[3:6])
