from array import array
import re



def getAncestors(n, edges):
    
    edges_reverse = [[] for _ in range(n)]
    for a,b in edges:
        # print (a,b)
        edges_reverse[b].append(a)
        
    def dfs(index):
        result = set()
        for element in edges_reverse[index]:
            result.add(element)
            result |= dfs(element) #or operation for sets
        return result
    ans_arr = []
    for i in range(n):
        ans_arr.append(sorted(dfs(i)))
    return ans_arr
    
    #you can write the above function as return [sorted(dfs(i)) for i in range(n)]
    #for in line return and less space
            
          





n = 8
edges  =  [[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]]       
print(getAncestors(n, edges))
