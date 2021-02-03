# =============================================================================
# # Exercise 1
# 
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# year = str((2021-age)+100)
# repeat = int(input("Amount of times to repeat the message: "))
# 
# for amount in range(repeat):
#     print(f"Hi {name}, you are {age} years old. You'll turn 100 in {year}")
# =============================================================================

# =============================================================================
# # Exercise 2: Check if number is even or odd
# 
# number = int(input("Enter a number: "))
# 
# if number % 2 == 0:
#     if number % 4 == 0:
#         print("The number is multiple of 4.")
#     else:
#         print("The number is even.")
# else:
#     print("The number is odd.")
# 
# num = int(input("Enter a number to check: "))
# check = int(input("Enter a number to divide: "))
# 
# division = num % check
# 
# if division == 0:
#     print("Number divides evenly.")
# else:
#     print("Number doesn't divide evenly.")
# =============================================================================


# =============================================================================
# # Exercise 3: https://www.practicepython.org/exercise/2014/02/15/03-list-less-than-ten.html
# 
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# 
# # =============================================================================
# # # List comprehension: 
# # # [do something for element in list if "condition"]
# # [print(element) for element in a if element < 5]
# # 
# # # List comprehension with ternary expression or operator: https://riptutorial.com/python/example/3226/conditional-expression--or--the-ternary-operator--
# # # [do something if "condition" else *do something else* for element in list ]
# # [print(element) if element < 5 else print(None) for element in a ]
# # =============================================================================
# 
# number = int(input("Enter a number: "))
# [print(element) for element in a if element < number]
# =============================================================================

# =============================================================================
# # Exercise 4: Divisors - https://www.practicepython.org/exercise/2014/02/26/04-divisors.html
# 
# number = int(input("Enter a number: "))
# check = list(range(1, number+1))
# divisors = list()
# 
# for element in check:
#     if number%element == 0:
#         divisors.append(element)
#         
# print(divisors)
# =============================================================================



























