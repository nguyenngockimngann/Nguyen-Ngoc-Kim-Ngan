# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 13:58:57 2024

@author: ASUS-PC
"""

def tinh_tong(*args):
    return sum(args)
print(tinh_tong(3,4,5,6)) 

def tinh_tich(*args):
    tich = 1
    for num in args:
        tich*=num
    return tich
print(tinh_tich(3,4,5,6))

