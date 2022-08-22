import math
def isPowerOfFour(n: int):
    return n>0 and math.log(n,4).is_integer()

print (isPowerOfFour(17))