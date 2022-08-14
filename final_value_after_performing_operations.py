from typing import final


def finalVal(operations):
    count = 0
    for i in operations:
        if i[1] == "+": #the array elements are strings, and the 0 th and 2nd changes but the 1th dont, 1thy always representing the operations. 
            #++X ---> + > 0 ; + > 1 ; X > 2 || X++ ---> X > 0 ; + > 1 ; + > 2
            count += 1
        else:
            count -= 1
    return count
                
       
operations = ["X++","++X","--X","X--"]

print(finalVal(operations))

