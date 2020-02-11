# C stands for circumference 
# d stands for denominator 

import math

def pi():
    n = eval(input("How many terms would you like to be summed: \n"))
    C = 4
    d = 1
    Sum = 0

    for i in range(n):
        Sum = (C/d) + Sum
        C = -1 * C
        d = d + 2
    print(Sum)
    print("The number calculate is", math.pi - Sum, "off from pi")

pi()

    


    
