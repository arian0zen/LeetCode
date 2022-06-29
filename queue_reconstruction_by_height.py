from queue import Empty


def reconstructQueue(people):
    queue = [[-1,-1]]*len(people)
    people.sort()
        
    for i,j in people: 
            
        greater_ele = 0
        place_pos = 0
                        
        while greater_ele<j:
            if queue[ place_pos ][0] >= i or queue[place_pos ][0] == -1:
                place_pos += 1
                greater_ele += 1
            else:
                place_pos += 1
            
        while queue[place_pos][0] != -1:
            place_pos+=1
            
        queue[ place_pos ] = [i,j]
    return queue
    
    
    
    
    

array = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
print(reconstructQueue(array))