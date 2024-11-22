""""
Rules for declaring variables
1. it should always start from a-z, A-Z, _(underscore)
2. variable can be anything from this after the start (a-z, A-Z, _(underscore), 0-9)
3. cannot start with a number or symbols 
4. cannot user reserved keywords


x=5
y=10
print(x+y)

# print (name)
# print(age)
# print(gender)

"""

"""
# Types of print:
1. Method 1 
print ('value')
print ('my name is', v1, v2, v3 ) (v1,v2,v3 --> where v is variable)
print ('my name is', v1, 'my age is', v2, 'my gender is 'v3' )

2. Method 2
using f strings we can print the multiple variables in one line.
syntax: print(f"statement {variable}")
print (f"My name is{variable 1} and my age is{variable 2}, my gender is{Variable 3}")

"""
# Examples:

name = "Shubham Jain"
age = 18
gender = "male"

# 1. Method 1


print(" My name is", name, "\n My age is", age, "\n My gender is", gender)
