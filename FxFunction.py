#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 16:52:54 2026

@author: thomas
"""

def Main(t):
    return t**3 + 8

if __name__ == "__main__":
    print(Main(9))
    if Main(9) > 27:
        print("YAY!")
    else:
        print("nay")
    

    