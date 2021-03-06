from re import A


def twoCitySchedCost(cost):
    
    n = len(cost)
    city_a = 0 
    city_b = 0
    min_cost = 0
    
    profit = [[0,0]]*len(cost)
    
    
    for i in range(len(cost)):
        profit[i]  = ((abs(cost[i][0] - cost[i][1])), i)
    profit.sort(reverse=True)
    # print (profit)
    # print(profit[i][1])
    
    for i in range(len(profit)):
        
        if (cost[profit[i][1]][1] <= cost[profit[i][1]][0] and city_b < n//2) or city_a == n//2:
            #(if it can to to b and also b in empty then) or a is full, we forcefully push them to b
            min_cost += cost[profit[i][1]][1]
            city_b += 1
            print(cost[profit[i][1]][1],  "space b:", city_b)
            
        elif city_a < n//2 : #else if, it can not go to b and also a is empty then push to a!! but if a is full the above conditions satisfies that means it goes b.
            #but is b is full, then all remaining all enters a until its full
            
            min_cost += cost[profit[i][1]][0]
            city_a += 1
            print("else",cost[profit[i][1]][0], "space a:", city_a)
        # print (min_cost)
                  
    
    return min_cost
 
    
costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
print(twoCitySchedCost(costs))
