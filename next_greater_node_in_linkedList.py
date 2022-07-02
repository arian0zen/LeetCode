# 1. at first we converted the linked list to an array! cause why not ? 
# 2. array gives us easier acces to iterate and implement stack for it
# 3. also, it takes only linear time so..
# 4. then we start iterating in reverse, for example an array of [5 3 1] will iterate as [1 3 5] #reverse iteration is important for monotonic stack (to find the NEXT)
# 5. then the real task, iterate the stack, untill we get last elem of stack which is less that arr[i] which is (1) for the above mentioned array, if it gets any such element in stack, it will keep poping that untill it gets an element that does not imply the conditions stack[-1] <= arr[i]
# 6. after the above steps, two things may happen either the stack is empty or the last elem of the stack is *the next greater* element
# 7. then if the stack is not empty, assign stack's last elem to ans[i]
# 8. and append the next arr element to stack!!
# 9. YOU MAY THINKK THAT there is a while loop inside a for loop it would be O(n^2). no it will only be O(n), cause if you see carefully the inside while loop is just having one operation POP. that is of constant time ! so it is overall O(n) onlyy

#okayy i tried my best to explain what is happening! and i agree i am not a good teacher! if you are having any doubt i will try to explainn further thank you!!
'''
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        arr = []
        current = head
        while current:
            arr.append(current.val)
            current = current.next
        # arr = arr[::-1]
        ans = [0] * len(arr)
        # print (ans)
        stack = []
        for i in reversed(range(len(arr))):
            while len(stack)> 0 and stack[-1] <= arr[i]:
                stack.pop()
            if len(stack)!= 0:
                ans[i] = stack[-1]
            stack.append(arr[i])
        return ans
            
'''

#this approach is 322 ms in leetcode