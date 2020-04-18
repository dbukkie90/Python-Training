# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 12:27:03 2020

@author: dbukk
"""

import math
π = math.pi
r = float(input("Enter radius of Circle:")) 
θ = float (input("Enter angle measure:"))
h= int(input("Enter number"))
b = int(input("Enter number"))
class computation:
    def triangleArea (b,h):
        res = (b*h)/2
        print (res)
    def circleArea (r):
        area = π * r**2
        print (area)
    def rectangleArea (l,b):
        area = l*b
        print (area)
        def side ():
            side = int(input("Enter side of square:"))
            area = side*side
            print ("Area of square = ", area) 
    def surface_area (): 
        surface_area = int(input("Enter surface area of cube:" ))
        area = 6*surface_area**2
        print  ("Area of cube = ", area)
    
    def area ():
        area = 2* π * r * h + 2 * π * r**2
        print ("Area of cylinder = ", area)

    def SectorArea ():
        SectorArea = (θ/360) * π * r**2
        if θ <=360:
            print (SectorArea)