def candy(ratings):
    length = len(ratings)
    min_candy = [1] * length
    for i in range(1, length):
        if ratings[i] > ratings[i-1] and min_candy[i] <= min_candy[i-1]:
            min_candy[i] = min_candy[i-1] + 1
    for i in reversed(range(len(ratings)-1)):
        print (i, i+1)
        if ratings[i] > ratings[i + 1] and min_candy[i] <= min_candy[i+1]:
               min_candy[i] = min_candy[i+1] + 1
    return sum(min_candy)
            
            
        # elif ratings[i] > ratings[i+1]:
        #     min_candy+= 1
        #     arr[i-1] += 1
        #     print(ratings[i-1], ratings[i], arr[i-1], arr[i], "7666")
        #     if ratings [i-1] > ratings[i] and arr[i-1] <= arr[i]:
        #         arr[i-1] += 1
        #         print(ratings[i-1], ratings[i], arr[i-1], arr[i], "kmao")
        #     if ratings [i+1] > ratings[i] and arr[i+1] <= arr[i]:
        #         arr[i+1] += 1
        #         print(ratings[i-1], ratings[i], arr[i-1], arr[i], "kgzfd")

ratings = [1,6,10,8,7,3,2]
print(candy(ratings))
# 1.first we are gonna check if i > i-1 (prev), if it is greater then increase one from its previous 's value
# 2.then a little trick, then we iterate in reverse to check if i > i+1 (for array of len 6, i = 5 4 3 2 1 0; when i = 5 we compare it with 6th elem, so basically we are cheking the front neighbour of the i th element) so if i is greater than i+1 th element as well, we change its candy count to min_candy[i+1] + 1)
# 3.in that way we will successfully compare an element with its previous and after's value! and change its candy count along the way..