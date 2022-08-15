# class Solution:
#     def romanToInt(self, s: str) -> int:

#         # First we create a hash dictionary with given keys and values.
#         hash_dict= {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

#         # Here we store the sum of numerals.
#         sum = 0

#         # Using for loop first we calculate the values for each and every numerals in 's' with the help of hash dictionary.   
#         for numerals in s:
#             sum += hash_dict[numerals]

#         # Here we are subtracting from sum if any of them present in this same order in 's'.

#         # Here 'IV' should be 1+5=6 generally? so if i substract(-) the 'IV' With 2 we get 6-2=4(THE RESULT WE WANT).
#         # Similarly for 'IX', 'XL' and others.

#         if 'IV' in s: 
#             sum -= 2
#         if 'IX' in s:
#             sum -= 2
#         if 'XL' in s:
#             sum -= 20
#         if 'XC' in s:
#             sum -= 20
#         if 'CD' in s:
#             sum -= 200
#         if 'CM' in s:
#             sum -= 200

#         # In the end we are returning our final sum.
#         return sum

# courtesy souvik