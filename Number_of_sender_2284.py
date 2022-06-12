import operator
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
        #Keymaxxx = max(hash_dict, value= lambda x: hash_dict[x])
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
                
            
                
        array.sort()    
        array = array[::-1]
        #print (array)
        print (array[0])
        #print (arr)
        
        
        
messages = ["Hello userTwooo","Hi userThree","Wonderful day Alice","Nice day userThree"]
senders = ["userOne","userTwo","userThree","userOne"]
largestWordCount(messages, senders)