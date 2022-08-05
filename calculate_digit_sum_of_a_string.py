def digitSum(s, k):
    
    
    if k >= len(s):
        return s
    
    rounded_array = ''
    for i in range(0, len(s), k):
        
        string = s[i:i+k]
        
        total = 0
        for each in range(len(string)):
            total += int((string[each]))
        rounded_array = rounded_array + (str(total))
       
    return digitSum(rounded_array, k)
    
    
    
 
s = "11111222223"
k = 3  
print(digitSum(s, k))
