import math

def isArmstrong__(x):
    
    digits = [int(digit) for digit in str(x)]

    k = math.floor(math.log(x, 10) + 1)
    
    return x == sum([digit ** k for digit in digits])


