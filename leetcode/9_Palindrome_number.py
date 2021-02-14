# https://leetcode.com/problems/palindrome-number/

x = 12321

# =============================================================================
# # First approach. Mathematical method: 68 ms, 14.3 mb
# # =============================================================================
# # Revert the number itself, and then compare the number with  original number,
# # if they are the same, then the number is a palindrome. However, if the reversed
# # number is larger than \text{int.MAX}int.MAX, we will hit integer overflow problem.
# # =============================================================================
# 
# # Negative numbers and numbers ending in 0 are not palindrome
# if x < 0 or (x % 10 == 0 and x != 0): print('Not palindrome') # return False
# x2 = x
# pop = 0
# reverted_number = 0
# 
# while x > 0:
#     pop = x % 10
#     reverted_number = reverted_number * 10 + pop
#     x = int(x / 10)
# 
# print(x2)
# print(reverted_number)
# 
# 
# if x2 == reverted_number:
#     print('Palindrome') # return True
# else: print('Not palindrome') # return False
# =============================================================================
    
# =============================================================================
# # Second approach. Same as First approach but reverting only half the number: 36 ms, 14.2 mb
# 
# # Negative numbers and numbers ending in 0 are not palindrome
# if x < 0 or (x % 10 == 0 and x != 0): print('Not palindrome') # return False
# 
# reverted_number = 0
# pop = 0
# 
# while x > reverted_number:
#     pop = x % 10
#     reverted_number = reverted_number * 10 + pop
#     x = int(x / 10)
# 
# if x == reverted_number or x == int(reverted_number/10):
#     print("Pal") # return True
# else: print("Not pal") # return False
# =============================================================================