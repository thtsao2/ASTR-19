#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 11:08:34 2026

@author: thomas
"""

class RedPanda:
    def __init__(self, arm_length, leg_length, eye_count, has_tail, is_furry):
        self.arm_length = float(arm_length)  
        self.leg_length = float(leg_length)  
        self.eye_count = int(eye_count)       
        self.has_tail = bool(has_tail)         
        self.is_furry = bool(is_furry)         

    def describe_animal(self):
        print("Characteristics of a Red Panda")
        print(f"Arm Length: {self.arm_length} cm")
        print(f"Leg Length: {self.leg_length} cm")
        print(f"Number of Eyes: {self.eye_count}")
        print(f"Has a tail: {'Yes' if self.has_tail else 'No'}")
        print(f"Is it furry: {'Yes' if self.is_furry else 'No'}")

my_favorite_animal = RedPanda(30.0, 25.0, 2, True, True)

my_favorite_animal.describe_animal()