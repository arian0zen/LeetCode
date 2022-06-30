#100% faster in leetcode
def reconstructMatrix(upper, lower, colsum):
    
    ans_array = []
    if sum(colsum) != upper + lower:
        return ans_array
    ans_array = [[0 for _ in range(len(colsum))] for _ in range(2)]
    upper_one = 0
    lower_one = 0
    for i in range(len(colsum)):
        if colsum[i] == 2:
            ans_array[0][i] = 1
            upper_one += 1
        
            ans_array[1][i] = 1
            lower_one += 1
        elif colsum[i] == 0:
            ans_array[0][i] = 0
            ans_array[1][i] = 0
        
                
    for i in range(len(colsum)):
        if colsum[i] == 1:
            if upper_one < upper:
                print (upper_one, upper)
                upper_one += 1
                ans_array[0][i] = 1
                
            else:
                lower_one += 1
                ans_array[1][i] = 1
    
    if upper_one != upper and lower_one != lower:
        return []
    
                      
    return ans_array           
    


upper = 5
lower = 5
colsum = [2,1,2,0,1,0,1,2,0,1]

print(reconstructMatrix(upper, lower, colsum))