#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 11:16:53 2026

@author: thomas
"""

import math

def main():
    n_entries = 1000
    start = 0.0
    end = 2.0
    step = (end - start) / (n_entries - 1)

    print(f"{'x':<10} | {'sin(x)':<10}")

    for i in range(n_entries):
        x = start + i * step
        sin_x = math.sin(x)
        print(f"{x:<10.4f} | {sin_x:<10.4f}")

if __name__ == "__main__":
    main()