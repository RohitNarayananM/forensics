# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 10:48:25 2021

@author: ASUS
"""
import base64
x="NFXGG5DGNJ5TI3K7ORUDGX2MGNAVG5C7GVUUO3RRMYYWGNDOKRPWEVKUL4YV6YZUJZPXI4RQOVBEYM27LEYHKXZUL5WDAVD5"

flag=base64.b32decode(x).decode()
print(flag)