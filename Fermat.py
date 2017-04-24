#!/usr/bin/env python
# -*- coding: utf-8 -*-
def fermat(n):
    x = 2**2**n + 1
    return x  

def teste(x):
        for i in range(2, x-1):  
            if x % i == 0:
                return False 

        return True 

sim = True
n = 1
while sim: 
    x=fermat(n)
    n += 1 
    sim=teste(x) 
    if sim:
        print('%s é primo' %x) 
    else:
        print('%s não é primo' %x)



