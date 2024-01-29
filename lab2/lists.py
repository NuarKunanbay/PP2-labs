#Examples
#1
thislist = ["apple", "banana", "cherry"]
print(thislist)
#2
thislist = ["apple", "banana", "cherry"]
print(len(thislist))
#3
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
#4
list1 = ["abc", 34, True, 40, "male"]
#5
mylist = ["apple", "banana", "cherry"]
print(type(mylist))
#6
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)
#7
thislist = ["apple", "banana", "cherry"]
print(thislist[1])
#8
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])
#9
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
#10
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])
#11
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])
#12
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])
#13
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
#14
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
#15
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
#16
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)
#17
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)
#18
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)
#19
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
#20
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)
#21
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
#22
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)
#23
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
#24
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)
#25
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
#26
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)
#27
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
#28
thislist = ["apple", "banana", "cherry"]
del thislist
#29
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
#30
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
#31
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])
#32
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
#33
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]
#34
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)
#35
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)
#36
newlist = [x for x in fruits if x != "apple"]
#37
newlist = [x for x in fruits]
#38
newlist = [x for x in range(10)]
#39
newlist = [x for x in range(10) if x < 5]
#40
newlist = [x.upper() for x in fruits]
#41
newlist = ['hello' for x in fruits]
#42
newlist = [x if x != "banana" else "orange" for x in fruits]
#43
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
#44
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)
#45
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)
#46
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)
#47
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
#48
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)
#49
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)
#50
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)
#51
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

#Exercises
#1
fruits = ["apple", "banana", "cherry"]
print(fruits)
#2
fruits = ["apple", "banana", "cherry"]
fruits[0] = 'kiwi'
#3
fruits = ["apple", "banana", "cherry"]
fruits.append('orange')
#4
fruits = ["apple", "banana", "cherry"]
fruits.insert("lemon")
#5
fruits = ["apple", "banana", "cherry"]
fruits.remove('banana')
#6
fruits = ["apple", "banana", "cherry"]
print(fruits[-1])
#7
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[3:6])
#8
fruits = ["apple", "banana", "cherry"]
print(len(fruits))

