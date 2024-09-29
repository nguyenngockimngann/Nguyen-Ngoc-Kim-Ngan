# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 14:12:46 2024

@author: ASUS-PC
"""

def tinh_chu_vi(*args, **kwargs):
    
    if kwargs.get('hinh') == 'vuong':
        canh = args[0] 
        return 4 * canh
    
    elif kwargs.get('hinh') == 'chunhat':
        chieu_dai, chieu_rong = args
        return 2 * (chieu_dai + chieu_rong)
    
    elif kwargs.get('hinh') == 'tron':
        ban_kinh = args[0]
        return 2 * 3.14159 * ban_kinh
    
    else:
        return "Hình không hợp lệ"

print(tinh_chu_vi(4, hinh='vuong'))  
print(tinh_chu_vi(5, 3, hinh='chunhat'))  
print(tinh_chu_vi(7, hinh='tron')) 
