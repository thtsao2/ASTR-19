#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 16:27:35 2026

@author: thomas
"""

def FloatingPointSum():
    Num1 = 16.5
    Num2 = 93.1
    print("The sum of", Num1, "and", Num2, "is", Num1+Num2)
    print(Num1+Num2, "is a", type(Num1+Num2))

def IntegerDifference():
    Num3 = 604
    Num4 = 5
    print("The difference between", Num3, "and", Num4, "is", Num3//Num4)
    print(Num3//Num4, "is a", type(Num3//Num4))
    
def ProductIntFloat():
    Num5 = 500
    Num6 = 5.1246
    print("The product of", Num5, "and", Num6, "is", Num5*Num6)
    print(Num5*Num6, "is a", type(Num5*Num6))

def Main():
    FloatingPointSum()
    IntegerDifference()
    ProductIntFloat()

if __name__ == "__main__":
    Main()