import random

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

# =============================================================================
# # Exercise 5: https://www.practicepython.org/exercise/2014/03/05/05-list-overlap.html
# 
# ## First Approach
# print("First approach:\n")
# 
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# common_elements = list()
# 
# # Get unique values
# a_unique = set(a)
# b_unique = set(b)
# 
# for i in a_unique:
#     for j in b_unique:
#         if i == j:
#             common_elements.append(j)
# 
# print(f"List a is: {a_unique}")
# print(f"List b is: {b_unique}")
# print(f"List of common elements is: {common_elements}\n")
# 
# ## Second approach: Random lists
# print("Second approach:")
# 
# a2 = list()
# b2 = list()
# common_elements2 = list()
# 
# # Filling first list: 15 elements
# for element in range(0,15):
#     n = random.randint(0, 50)
#     a2.append(n)
# 
# # Filling second list: 10 elements
# for element in range(0,10):
#     n = random.randint(0, 50)
#     b2.append(n)
# 
# # Get unique values
# a2_unique = set(a2)
# b2_unique = set(b2)
# 
# for i in a2_unique:
#     for j in b2_unique:
#         if i == j:
#             common_elements2.append(j)
# 
# # Sort final list
# common_elements2.sort()
# 
# print(f"List a is: {a2_unique}")
# print(f"List b is: {b2_unique}")
# print(f"List of common elements is: {common_elements2}")
# =============================================================================

# =============================================================================
# # Exercise 6: https://www.practicepython.org/exercise/2014/03/12/06-string-lists.html
# 
# string = input("Enter a string: ")
# 
# #Make sure everything is lowercase
# string = string.lower()
# 
# 
# # Delete spaces
# if ' ' in string:
#     string = string.replace(' ','')
# 
# 
# #palindrome = "".join(list(reversed(string)))
# # Instead of reverse we can use: palindrome = string[::-1]
# # Source: https://stackoverflow.com/questions/31633635/what-is-the-meaning-of-inta-1-in-python
# 
# palindrome = string[::-1]
# 
# if string == palindrome: print("Palindrome")
# else: print("Not palindrome")
# 
# 
# # Using functions:
#     
# def palindrome(word):
#     if ' ' in word:
#         word = word.replace(' ', '')
#     palindrome = reversed(word) #word[::-1]
#     for letter, rev_letter in zip(word, palindrome):
#         if letter != rev_letter:
#             return 'Not Palindrome'
#     return 'Palindrome'
# 
# word = input("Input a string: ")
# result = palindrome(word)
# 
# print(result)
# =============================================================================
