# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 06:36:19 2020

@author: dbukk
"""

'''
#Assignment

#Area of a Circle = πr^2
'''
import math
π = math.pi
print (π)
def circleArea (r):
    area = π * r**2
    print (area)
r=6
circleArea (r)


'''
#Area of Rectangle = l*b
'''
def rectangleArea (l,b):
    area = l*b
    print (area)
l = 4
b = 6
rectangleArea (l,b)


'''
#Area of a Square = l*l
'''
side = int(input("Enter side of square:"))
area = side*side
print ("Area of square = ", area)


'''
#Area of cube = 6a**2
'''
surface_area = int(input("Enter surface area of cube:" ))
area = 6*surface_area**2
print  ("Area of cube = ", area)


'''
#Area of Cylinder = 2πrh + 2πr**2
'''
import math
π = math.pi
r = 5
h = 9

area = 2* π * r * h + 2 * π * r**2
print ("Area of cylinder = ", area)


'''
#Area of a Sector in degrees = (θ/360) * π * r**2
'''
import math
def SectorArea ():
    r = float(input("Enter radius of Circle:")) 
    θ = float (input("Enter angle measure:"))
    π = math.pi
    SectorArea = (θ/360) * π * r**2
    if θ <=360:
        print (SectorArea)




    

