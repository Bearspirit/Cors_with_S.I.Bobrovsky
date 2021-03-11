""" Вступительная задача"""
import random


def func(t1, t2):
    for i in range(0, len(t1)-len(t2)+1): 
        for m in range(0, len(t2)):
            if t1[i+m] != t2[m]: 
                break                 
        else:
            return True 
    return False                

