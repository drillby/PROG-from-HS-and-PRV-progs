# ax^2 + bx + c = 0     -> 2, 1
# 4x^2 + 8x -50 = 0

# x1,2 = ( -b +- sqrt(D) )  / 2a

import math


def linearni_rovnice(b,c):
    if b == 0:
        if c == 0:
            return "Celé R"
        else:
            return None
    else:
        return -c/b


def kvadraticka_rovnice(a,b,c):
    Diskriminant = b**2 - 4*a*c
    
    if a==0:  # linearni rovnice
        return [ linearni_rovnice(b,c) ]
    
    if Diskriminant < 0:
        return []
    elif Diskriminant == 0:
        return [ -b/(2*a) ]
    else:
        return [ (-b - math.sqrt(Diskriminant)) / (2*a) ,
                 (-b + math.sqrt(Diskriminant)) / (2*a) ]
    
    
print(kvadraticka_rovnice(8,10,5))