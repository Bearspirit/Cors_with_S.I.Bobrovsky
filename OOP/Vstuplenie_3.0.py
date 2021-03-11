""" Вступительная задача"""

def func(t1, t2):
    if len(t2) > len(t1): 
        return False
    else:
        for i in range(0, len(t1)): 
            m = 0
            k = i
            while k < len(t1) and m < len(t2): 
                if t1[k] != t2[m]: 
                    break 
                elif k == len(t1)-1 and len(t2)>1: 
                    break
                else: 
                    m += 1
                    k += 1                   
            else:
                return True 
        return False                
                            
print(func("012345", "01"))