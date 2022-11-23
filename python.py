print("Hello World")

a = int(8) + int(9)
print(a)

number = 18
print(float(18))

name = "Tony Starrk"

print(name.upper())
print(name.find('S'))  
print(name.replace("Tony Starrk","Ironman"))
print(name)
print('r' in name)
print(5 ** 2)

""" Operator Precedance """ # - comment
# hello - comment
result = 2 + 3 * 5
print(result)

""" Arithemetic operator"""
# +	    Addition	    x + y	
# -	    Subtraction	    x - y	
# *	    Multiplication	x * y	
# /	    Division	    x / y	
# %	    Modulus	x % y	
# **	Exponentiation	x ** y	
# //	Floor division	x // y	:- gives floor value 

"""Python Comparison Operators"""

# Operator	Name	                  Example	Try it
# ==	    Equal	                  x == y	
# !=	    Not equal	              x != y	
# >	        Greater than	          x > y	
# <	        Less than	              x < y	
# >=	    Greater than or equal to  x >= y	
# <=	    Less than or equal to	  x <= y

"""Logical Operators"""

# Operator	   Description	                         Example	Try it
# and 	Returns True if both statements are true	x < 5 and  x < 10	
# or	Returns True if one of the statements is true	x < 5 or x < 4	
# not	Reverse the result, returns False if the result is true	not(x < 5 and x < 10)

""" Conditional Satetment"""
age = 18
if age> 18:
    print("ok")
elif age<18:
        print("not ok")
else:
    print("good night")

"""While loop"""

i=1
while i<=5:
   print(i)
   i = i+1


while i <= 5:
    print(i * "*")
    i += 1

"""For loop"""

for i in range(1,5):
    # here range(1,5) means it will go from 1 to 4 not 5.
    print(i + 1)

""" List"""

marks=[34,56,"gj"]
print(marks[2])
print(marks[1:3]) # between 1 to 3 means 2 and 3

marks.append(99) # to add number at last
# marks.insert(76) - to add number at first
print(marks)
print(len(marks))
for item in marks:
    print(item)

"""Break and continue"""

school =["one","two","three","four","five"]

for student in school :
    if student == "three":
       continue; # it will skip below number
    if student == "five":
        break;
    print(student)

""" Tuple"""

#Tuples are ordered, indexed collections of data
#Tuples can store duplicate values
#You cannot change the data of a tuple after that you have assigned it the values
#Like lists, it can also store several data items
# tuples are immutable
# initialize tuple

scores = (10, 20, 30)

# check if 10 is in scores tutple
print(10 in scores)

# print all scores in tuple
for score in scores:
    print(scores)

# print length of tuple
print(len(scores))

# print scores reversed
print(tuple(reversed(scores)))

# print scores reversed
print(scores[::-1])

# print first score by index
print(scores[0])

# print first two scores
print(scores[0:2])

# print tuple
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

marks= (84,56,34,33)

person = "Tony" ,"John","kishan" # this is also tuple

"""Sets"""

myset = {"apple", "banana", "cherry"}

#A set is a collection which is unordered, unchangeable*, and unindexed.
# note : -  Set items are unchangeable, but you can remove items and add new items.
# set only stores uniq value 

marks = {84,56,34,33,33}
print(marks)
# it will not give 33 two times because it stores only uniq values
# index doesn't exist in sets
# we have to use loop to print ir

for i in marks:
    print(i)

""" Dictonary"""
marks = {"english": 90 , "maths" : 82,"SS" : 90}
#it's like object

print(marks["maths"])

marks["maths"] = 99;
print(marks)
#Creating dictionaries
dict1 = {'color': 'blue', 'shape': 'square', 'volume':40}
dict2 = {'color': 'red', 'edges': 4, 'perimeter':15}

#Creating new pairs and updating old ones
dict1['area'] = 25 #{'color': 'blue', 'shape': 'square', 'volume': 40, 'area': 25}
dict2['perimeter'] = 20 #{'color': 'red', 'edges': 4, 'perimeter': 20}

#Accessing values through keys
print(dict1['shape'])

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])

"""Use defined functionn"""

def myfunc(x,y):
    print(x+y)
    

myfunc(1,5)