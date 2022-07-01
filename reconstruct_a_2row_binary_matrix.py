#100% faster in leetcode
def reconstructMatrix(upper, lower, colsum):
    
    ans_array = []
    if sum(colsum) != upper + lower:
        return ans_array
    ans_array = [[0 for _ in range(len(colsum))] for _ in range(2)]
    for i in range(len(colsum)):
        if colsum[i] == 2:
            ans_array[0][i] = 1
            upper -= 1
        
            ans_array[1][i] = 1
            lower -= 1
        elif colsum[i] == 0:
            ans_array[0][i] = 0
            ans_array[1][i] = 0
        
                
    for i in range(len(colsum)):
        if colsum[i] == 1:
            if upper!=0:
                # print (upper)
                upper -= 1
                ans_array[0][i] = 1
                
            elif lower!= 0:
                # print (lower)
                lower -= 1
                ans_array[1][i] = 1
    
    if upper!= 0 and lower != 0:
        return []
    
                      
    return ans_array           
    


upper = 5
lower = 5
colsum = [2,1,2,0,1,0,1,2,0,1]

print(reconstructMatrix(upper, lower, colsum))