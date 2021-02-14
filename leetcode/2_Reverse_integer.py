# https://leetcode.com/problems/reverse-integer/

x = -11234544615
negative = False

# Check if number is negative. If it is, make it positive to reverse it.
if x < 0:
    x *= -1
    negative = True

# =============================================================================
# # First approach - mathematical method: 28 ms, 14.3 mb
# pop = 0
# num_reversed = 0
# 
# while x > 0: # pop and divide
#     pop = x % 10
#     num_reversed = num_reversed * 10 + pop
#     x /= 10
#     x = int(x)
# 
# if negative:
#     num_reversed *= -1
# 
# if num_reversed.bit_length()>31:
#     print("Number too big or small: return 0") # return 0
# else: print(f"Number reversed: {num_reversed}") # return num_reversed
# =============================================================================

# =============================================================================
# # Second approach - pythonic method: 16 ms, 14.3 mb
# # Convert to string to easily reverse it. Reverse it. Convert Back
# num_reversed = int(str(x)[::-1])
# 
# # If the number was negative, make the reversed number negative as well
# if negative: num_reversed *= -1
#     
# if num_reversed.bit_length()>31:
#     print("Number too big or small: return 0") # return 0
# else: print(f"Number reversed: {num_reversed}") # return num_reversed
# 
# # =============================================================================
# # # This could also be used
# # if num_reversed >= (2**31-1) or num_reversed <= (-2**31):
# #     print("Number too big or small: return 0") # return 0
# # else: print(f"Number reversed: {num_reversed}") # return num_reversed
# # =============================================================================
# =============================================================================
