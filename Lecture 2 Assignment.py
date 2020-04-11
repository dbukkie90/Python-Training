# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 16:05:47 2020

@author: dbukk
"""

'''
print ((4<5) and (5>6))
print ((1==2) or (2==2))
print ((4<5) and (5<6))

if (1==2) or (2==2):
    print (True)
'''

'''    
spam = 0
while (spam<5):
    print ("Hello World")
    spam = spam + 1
    if (spam==3):
        break
print ("Thank you")
'''

'''
spam = 0
while (spam<5):
    print ("Hello World")
    spam = spam + 1
    if (spam==3):
        continue
'''

'''
i = 10
while i <= 10:
    print "Enter the first number"
    i = i+1
'''

'''
i = 10
while i > 0:
    print ("Enter number")
i = int (input())
result = i + 1
print ("average" (result /10))
'''

'''
i = 0
while i < 10:
    print ("Enter number")
    i = i + 1
print (i/10)
'''

'''
i = 1
while i <= 4:
    print ("*"*i)
    i = i+1
'''

'''
a = 1
b = 2
while a >= 1:
    i = " "*b+"*"*a+" "*b
    print ("a")
    i = i+2
    b = b-1
    if i>5:
        break
i = 3
b = 1
while i>=1:
    a = " "*b+"*"*i+" "*b
    print("a")
    i = i-2
    b = b+1
'''

'''
i = 1
while i <= 4:
    print (1*i)
    i = i+1
'''

'''
i = 1
while i <= 10:
    print (24*i)
    i = i+1
'''

'''
while True:
    print ("My name is Dami")
'''

'''
def factorial (x):
    if x==1:
        return 1
    else:
        return x * factorial (x-1)
print (factorial (24))
'''

'''
def get_gcd	(x, y):
 
   while(y):
       x, y = y, x % y
 
   return x
 
n1 = 48
n2 = 36
 
hcf = get_gcd(n1,n2)
print("Highest Common Factor = ", hcf)
'''

'''
def computegcd(x,y):
    if x>y:
        small = y
    else:
        small = x
    for i in range(1, small+1):
         if((x % i == 0) and (y % i == 0)):
            gcd =i
    return gcd

x = 60
y = 48
hcf = computegcd(x,y)
print("Highest Common Factor = ", hcf)
'''


while True:
    a = raw_input (Print ("average and product of all numbers")
    int = input (int >=1)
    int_1 = input(1)
    int_2 = input (2)
    total = int_1+int_2
    average = total/2
    product = int_1*int_2
    
    a=raw_input (Print ("average and product of all numbers")
    int = input (int >=1))
    if a == "q":
        break
    

