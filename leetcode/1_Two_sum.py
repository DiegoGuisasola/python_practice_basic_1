# From: https://leetcode.com/problems/two-sum/

nums = [3,3]
target = 6
list_of_indeces = list()

# =============================================================================
# # First approach: 812 ms, Memory Usage: 14.3 MB
# for i in range(len(nums)-1):
#     j = i + 1
#     while j <= len(nums)-1:
#         if nums[j]+nums[i] == target:
#             list_of_indeces.append(i)
#             list_of_indeces.append(j)
#         j += 1
#                 
# 
# print(list_of_indeces)
# =============================================================================

# =============================================================================
# # Second approach: 488 ms, Memory Usage: 14.5 MB
# for i in range(len(nums)-1):
#     for j in range(i+1, len(nums)):
#         if nums[j]+nums[i] == target:
#             list_of_indeces.append(i)
#             list_of_indeces.append(j)
#                 
# print(list_of_indeces)
# =============================================================================

# =============================================================================
# # Third approach: 40 ms, Memory Usage: 14.5 MB
# for i, inum in enumerate(nums): # In this case enumerate return a tuple from a list: (index, value)
#     for j, jnum in enumerate(nums[i+1:], i+1):
#         if (inum + jnum == target): print( [i, j])
# =============================================================================





