from cmath import sqrt
import math
from msilib import sequence
import re

 #try the edge case where num is == 1
def closestDivisors(num):
    n = num + 1
    m = num + 2
    b = math.sqrt(n)
    b = math.ceil(b)
    c = math.sqrt(m)
    c = math.ceil(c)
    dif_counter = num
    # one = num
    print (c)
    
    i = 1
    for i in reversed(range(1, c+1)):
        #print(i)
        if m % i ==0:
            if (m / i == i):
                dif_counter = 0
                #print (abs(i - int(m/i)))
                return(i, i)
            
            elif ((abs(i - int(m/i))) <= dif_counter) :
                one = (abs(i - int(m/i)))
                dif_counter = (abs(i - int(m/i)))
                return (i, int(m/i))
                
        elif n % i ==0:
            if (n / i == i):
                dif_counter = 0
                
                return(i, i)
            elif ((abs(i - int(n/i))) <= dif_counter) :
                dif_counter = (abs(i - int(n/i)))
                return (i, int(n/i))
                
        
    
print(closestDivisors(24))
    
    
    
    
    
    
    
    
    
    
    


















'''

Given an integer num, find the closest two integers in absolute difference whose product equals num + 1 or num + 2.

Return the two integers in any order.

 

Example 1:

Input: num = 8
Output: [3,3]
Explanation: For num + 1 = 9, the closest divisors are 3 & 3, for num + 2 = 10, the closest divisors are 2 & 5, hence 3 & 3 is chosen.
Example 2:

Input: num = 123
Output: [5,25]
Example 3:

Input: num = 999
Output: [40,25]


'''