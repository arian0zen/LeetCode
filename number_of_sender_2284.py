import operator
import random
def largestWordCount(messages, senders):
        length = len(messages)
        m = messages
        s = senders
        i = 0
        #print (length)
        n = length + 1
        
         
        hash_dict = {}
        #arr = []
        updated_table = {}
        for i in range(len(m)):
            
            #print (i)
            if s[i] in hash_dict:
                hash_dict[s[i]] += (m[i].count(' ')) + 1
            else:
                
                hash_dict[s[i]] = (m[i].count(' ')) + 1
            #arr.append(s[i])
        
        #hash_dict.sort()
        #sorted(hash_dict.items())
        keymax = max(hash_dict.items(), key = operator.itemgetter(1))[0]
        #Keymax = max(hash_dict, value= lambda x: hash_dict[x])
        #hash_dict.values().sorted()
        #for each in sorted (hash_dict.values()):
            #print (each)
            #dict['key3'] = 'Geeks'
        #hash_count = {}
        #hash_count[hash_dict[0]] = 6
        #for each in 
        
        #for each in 
        #print(hash_dict.values())
        #position = hash_dict.index(key)
        #print(key_list[position])
        
        #for each in hash_dict:
            #print (each)
            #if hash_dict[each]
        
        
        #print (hash_dict[Keymax])
        array = []
        
        
        for each in hash_dict:
            if (hash_dict[keymax]) == hash_dict[each]:
                array.append(each)
                
            
         #using quick select to get the last element
        def partition(arr, l, r, ):
            random_i = random.randint(l, r)
            arr[l], arr[random_i] = arr[random_i], arr[l]
            pivot, j = arr[l], l
            #print (arr[l], j)
            for i in range(l + 1, r + 1):
                if arr[i] < pivot:
                    j += 1
                    arr[i], arr[j] = arr[j], arr[i]
            arr[l], arr[j] = arr[j], arr[l]
            #print( arr[j], j)
            return j
    	    
        
        def maxElement(arr, l, r, max):
            
            if (max > 0 and max <= r-l+1):
                pivot_index = partition(arr, l , r)
                
                if (pivot_index-l == max-1):
                    return arr[pivot_index]
                if (pivot_index-l > max-1):
                    return maxElement(arr, l, pivot_index-1, max)
                #else when pivot_index < max-1, return
                return maxElement(arr, pivot_index+1, r, max-pivot_index+l-1)
            else:
                return ("kya kar rha bhai tu?")
            
            
        print (array)    
        n = len(array)
        #print (n)
        maximum = n
        largest = maxElement(array, 0, n-1, maximum)
        print (largest)
        # array.sort()    
        # array = array[::-1]
        # print (array)
        # print (array[0]) #if we use sort function to get the last element it will take O(n log(n)) time instead we can use QUICKSelect function to get the last element in O(n) time
        #print (arr)
        
        
        
messages = ["Hello userTwooo","Hi userThree","Wonderful day Alice and and","Nice day userThree", "blah blah blah blah blah"]
senders = ["random","userTwo","userzhree","random", "userone"]
largestWordCount(messages, senders)
