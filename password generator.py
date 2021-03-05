# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 14:40:35 2021

@author: dell
"""
import random
    
UPPERCASE=['A','B','C','D']
lowercase=['a','b','c','d']
number=['1','2','3','4']
specialcharacter=['#','$','%','&']
while True:
        len=int(input("enter the length"))
        count=int(input("how many password do you want to generate"))
        for x in range(0,count):
            password=""
            for x in range(0,len):
            
                password=random.choice(UPPERCASE)+random.choice(lowercase)+random.choice(number)+random.choice(specialcharacter)
                password=password+password
            print("your new password is:", password)
    