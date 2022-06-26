from multiprocessing import cpu_count


#a naive solution that is not working properly

def minDistance(word1, word2) :
        
    def sliding_window(word1, word2): 
        n = len(word1)
        a = word1
        b = word2  
        #initialize the sliding window
        count = len(a)
        
        end = 0
        for end in range(n):
            start = 0
            a = word1
            a = a.replace(a[end:end+1], '', 1)
            print(a)
            print(start)
            while start < n:
                b = word2
                b = b.replace(b[start:start+1], '', 1)
                print (b, start)
                if b == a:
                    count = min(count, end - start+1)
                    # print(count)
                
                else:
                    start+= 1
              
        return count
            
 
    if len(word1) > len(word2):
        return len(word1) - len(word2)
    elif len(word1) < len(word2):
        return len(word2) - len(word1)
    else:
        return sliding_window(word1, word2)
     
        
a = "sea"
b = "ate"        
print(minDistance(a,b))
        # if len(word1) == len(word2):
        #     for char in range(len(word1)):
        #         if word1[char] not in word2:
        #             count += 1
        #             # print (word1[char])
                    
        #     return count * 2