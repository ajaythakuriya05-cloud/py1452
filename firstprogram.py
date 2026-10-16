# Python first program:

# print("Apna College")
# print("My name is ajay kumar kol")
# print("I am 18 year old")
# print("my name is ajay kumar kol, my age is 18")

# Character sets:

# print(18)
# print(22)
# print(18+22)

# Variables: 

# name = "Ajay"
# age = 18
# price = 22

# print("my name is:", name)
# print("my age is:", age)
# print("my price is:", price)       

# Data types:

# 1. integers = +ve, -ve, 0 : int = 18,-22,0, etc.
# 2. Strings = '', "", '''''' : str = 'ajay',"kumar",'''kol''', etc.
# 3.Floats = 1.8, 2.00, 22.0 : decimal no. are include.
# 4. Boolean = True, False : currently age= 18, old age= false.
# 5. none = a = none.

# age = 18           
# name = "Ajay"
# value = 22.2
# old = True
# a = None


# print(type(age))      : type'int'
# print(type(name))     : type'str'
# print(type(value))    : type'float'
# print(type(old))      : type'boolean'
# print(type(a))        : type'none'

# Print sum:

# a = 100
# b = 300
# sum = a+b
# print(sum)

# a = 500
# b = 200
# subtract = a-b
# print(subtract)

# Comments in python:

#. single line comment 
#. multi line comment 
# print("I 'am jay")        
# shortkeys = control+forwardslace.

# Types of operators:

# Arithmetic operators:
# a = 10
# b = 3
# print(a + b) :   sum operator
# print(a - b) :   subtract operator
# print(a * b) :   multiple operator
# print(a / b) :   division operator
# print(a % b) :   modulus operator  = remainder
# print(a**b)  :  power operator = exponential

# Relational operators:
# a = 40
# b = 20
# print(a == b) :  False
# print(a != b) :  True
# print(a >= b) :  True
# print(a > b)  :  True
# print(a <= b) :  False
# print(a < b)  :  False

# Assignment operators:       = sign is name asign

# num = 10
# num += 10
# print("num:", num)  : 20

# num = 10
# num -= 10
# print("num:", num)  : 0

# num = 10
# num *= 5
# print("num:", num)  : 50

# num = 10 
# num /= 5
# print("num:", num)  : 2.0

# num = 20
# num %= 10
# print("num:", num)  : 0

# num = 20
# num **= 10
# print("num:", num)  : 1024000000000


# Logical operators:

# a = 50
# b = 30
# print("Not True")

# val1 = True
# val2 = False
# print("And", val1 and val2)

# a = 50
# b = 30
# print("Or", (a==b) or (a>b))

# Type conversion:

# conversion : automatically
# a = 2
# b = 4.5           : float coverts into int value.
# sum = a + b           then, sum a+b = 6.5       
# print(sum)               without errors.

# casting : manually
# a = "2"             : because string are not exits 
# b = 4.65                for casting types is error.
# sum = a + b             they form as int,float,etc.
# print(sum)                int("2") is right form.

# String:   string is type that store a squence of characcters.

# Basic operators = concatenation:  "hello"+"world" = "Helloworld"

# str1 = "apna"
# str2 = "college"
# print(str1+str2)

# length of strings:    len(str)   :    count always space, percentage, etc.

# str1 = "vikrant"
# len1 = len(str1)
# print(len1)
# str2 = "institution"
# len2 = len(str2)
# print(len2)

# final_str = str1 +" "+ str2
# print(final_str)
# print(len(final_str))


# Indexing:   index : position
# ajay_kumar : 0123456789

# str = "vikrant"     : could not be change character
# print(str[3])
 
# Slicing:      accessing part of  a string : +ve

# str = "Vikrant institution"
# print(str[:7])        : [0:7]
# print(str[8:])        : [8:len(str)]


# Negative index
# Apple : -5-4-3-2-1

# str = "apple"
# print(str[-5:])


# String functions:

# 1. str.endwith("")   : returns true if string ends.
# str = "i am studying python from apna college"
# print(str.endswith("ege"))

# 2. str.capitalize()   : capitalizes character.
# str = "currently i persued b.tech computer science in vikrant group of instution"
# print(str.capitalize())

# 3. str.replace(old,new)   : replaces all occurrences old.
# str = "I am 18 years old"
# print(str.replace("18","22"))

# 4. str.find(word)     : returns 1st index of 1st occurer.
# str = "I am thankfull my family"
# print(str.find("my"))

# 5. str.count("am")    : count the occurences of string.
# str = "Those are my weakness"
# print(str.count("a")) 


#  If(condition) : statement1
# age = 22

# if(age >= 18):
#     print("I am young")

# elif(condition): statement2
# light = "green"             : infinite condition allows

# if(light == "red"):
#     print("stop") 
# elif(light == "green"):
#     print("go")
# elif(light == "yellow"):
#     print("look")

# else(conditon): statement3
# age = 18

# if(age >= 22):
#     print("can vote")

# else:
#     print("cannot vote")

# marks = int(input("enter a student marks: "))

# if(marks >= 90):
#     grade = "A"
# elif(marks >= 80 and marks < 90):
#     grade = "B"
# elif(marks >= 70 and marks < 80):
#     grade = "C"
# else:
#     grade = "D"

# print("grade of the student >", grade)

# Tab = Indentation        : = Collen

# let's practice: Question

# 1. Write a program to check if a number entered by the user is odd or even.

# number = int(input ("enter a number"))
# if(number % 2 == 0):
#     print("even")
# else:
#     print("odd")

# 2. Write a program to find greatest of 3 numbers entered by the user.

# a = int(input("enter first number: "))
# b = int(input("enter second number: "))
# c = int(input("enter third number: "))

# if (a >= b and a>= c):
#     print("first number is largest", a)
# elif(b >= c):
#     print("second number is largest", b)
# else:
#     print("third number is largest", c)



