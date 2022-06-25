from calendar import c
from itertools import count
from re import M
import re



#solve later using SLIDING WINDOW technique, 2 pointers 26_06_2022

def balancedString(s):
    
    hash_dict = {"Q": 0, "W": 0, "E": 0, "R": 0}
    hash_dict["Q"] = s.count('Q')
    hash_dict["W"] = s.count('W')
    hash_dict["E"] = s.count('E')
    hash_dict["R"] = s.count('R')
       
       
    count = len(s)   
    must_appear = len(s) // 4
    left = 0
    right = 0
    for right in range(len(s)):
        hash_dict[s[right]] -= 1
        
        while left < len(s) and hash_dict["Q"] <= must_appear and hash_dict["W"] <= must_appear and hash_dict["E"] <= must_appear and hash_dict["R"] <= must_appear:
            count = min(count, right - left+1)
            hash_dict[s[left]] += 1
            left += 1
            print (right)
            
    return count
        
            
s = "WWEQERQWQWWRWWERQWEW"
print(balancedString(s))


















'''

 n = len(s)
    print ("length",n)
    must_appear = n // 4
    
    
    hash_dict = {"Q": 0,
                 "W": 0,
                 "E": 0,
                 "R": 0}
    
    count = 0
    hash_dict["Q"] = s.count('Q')
    hash_dict["R"] = s.count('R')
    hash_dict["E"] = s.count('E')
    hash_dict["W"] = s.count('W')
    print (hash_dict)
    
    if hash_dict["Q"] and hash_dict["R"] and hash_dict["E"] and hash_dict["W"] == must_appear:
        return 0
    if hash_dict["Q"] > must_appear:
        count += hash_dict["Q"] - must_appear
    if hash_dict["R"] > must_appear:
        count += hash_dict["R"] - must_appear
    if hash_dict["W"] > must_appear:
        count += hash_dict["W"] - must_appear
    if hash_dict["E"] > must_appear:
        count += hash_dict["E"] - must_appear
    
    return count
    

'''