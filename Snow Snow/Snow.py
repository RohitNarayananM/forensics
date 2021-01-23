# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 21:27:45 2021

@author: ASUS
"""

x="ntio{eP1B35x4K3_aB3O0_q5_K00t}"
flag=''
for i in x:
    if(i.isupper()):
        flag+=chr((ord(i)-8-65)%26+65)
    elif(i.islower()):
        flag+=chr((ord(i)-8-97)%26+97)
    else:
        flag+=i
print(flag)