from operator import le
from queue import Empty


def reconstructQueue(people):
    queue = [[]]
    people.sort(key=lambda x: [-x[0], x[1]])
    # people.sort(key = lambda x: x[1])
    # print (people)
    for i in range(len(people)):
        queue.insert((people[i][1]), people[i])
        # print (queue)
    queue.pop()
    return queue
    
    
    
    
    
    

array = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
print(reconstructQueue(array))