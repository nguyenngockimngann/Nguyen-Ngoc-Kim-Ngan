# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 14:33:28 2024

@author: ASUS-PC
"""

def tinh_toan(*args, **kwargs):
    hinh = kwargs.get('hinh')
    
    if hinh == 'vuong':
        canh = args[0]
        chu_vi = 4 * canh
        dien_tich = canh * canh
        return {'chu_vi': chu_vi, 'dien_tich': dien_tich}
    
    elif hinh == 'chunhat':
        chieu_dai = args[0]
        chieu_rong = args[1]
        chu_vi = 2 * (chieu_dai + chieu_rong)
        dien_tich = chieu_dai * chieu_rong
        return {'chu_vi': chu_vi, 'dien_tich': dien_tich}
    
    elif hinh == 'tron':
        ban_kinh = args[0]
        chu_vi = 2 * 3.14159 * ban_kinh
        dien_tich = 3.14159 * ban_kinh * ban_kinh
        return {'chu_vi': chu_vi, 'dien_tich': dien_tich}
    
    else:
        return 'Hình không hợp lệ'

ket_qua_vuong = tinh_toan(5, hinh='vuong')
print(f"Hình vuông - Chu vi: {ket_qua_vuong['chu_vi']}, Diện tích: {ket_qua_vuong['dien_tich']}")

ket_qua_chunhat = tinh_toan(5, 10, hinh='chunhat')
print(f"Hình chữ nhật - Chu vi: {ket_qua_chunhat['chu_vi']}, Diện tích: {ket_qua_chunhat['dien_tich']}")

ket_qua_tron = tinh_toan(7, hinh='tron')
print(f"Hình tròn - Chu vi: {ket_qua_tron['chu_vi']}, Diện tích: {ket_qua_tron['dien_tich']}")
