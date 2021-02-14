s = "MCMXCIV"
# =============================================================================
# reversed_s = s[::-1]
# 
# number = 0
# rom = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
# 
# number = rom[reversed_s[0]]
# 
# for c in range(1, len(reversed_s)):
#     if rom[reversed_s[c]] < rom[reversed_s[c-1]]:
#         number -= rom[reversed_s[c]]
#     else:
#         number += rom[reversed_s[c]]
# 
# print(number) # return number
# =============================================================================

# =============================================================================
# # To analyse
# r = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
# result = 0
# for x in range(0, len(s)):
#     if x > 0 and r[s[x]] > r[s[x-1]]:
#         take_away = r[s[x]] - r[s[x-1]]
#         result += take_away - r[s[x-1]]
#         print(f"1 {result}")
#     else:
#         result += r[s[x]]
#         print(f"2 {result}")
# =============================================================================

