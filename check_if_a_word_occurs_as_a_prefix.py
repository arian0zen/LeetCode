def isPrefixOfWord(sentence, searchWord):
    temp_a = sentence.split(' ')
    print(temp_a)
    for i in range(len(temp_a)):
    	if temp_a[i].startswith(searchWord):
            return i + 1

    return -1

        
	
    
	
 
sentence = "leetcode corona"
searchWord = "leet"
print(isPrefixOfWord(sentence, searchWord))
        
