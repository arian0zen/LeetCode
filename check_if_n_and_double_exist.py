def double(arr):
    hash_dict = {}
    for i in arr:
        if i in hash_dict:
            return True
        else:
            hash_dict[i*2] = True
            hash_dict[i/2] = True
    return False   
    
    
arr = [7,1,14,11]
print(double(arr))