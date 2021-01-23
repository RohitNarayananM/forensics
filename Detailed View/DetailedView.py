# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 22:11:44 2021

@author: ASUS
"""

import base64

x="ZmxhZ3tNMTVzSTBOX2FDYzBNUEwxNWgzRH0="
flag=base64.b64decode(x).decode()
print(flag)