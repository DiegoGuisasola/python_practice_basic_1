import random
import sys

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

# =============================================================================
# # Exercise 7: https://www.practicepython.org/exercise/2014/03/19/07-list-comprehensions.html
# 
# # =============================================================================
# # # List comprehension: 
# # # [do something for element in list if "condition"]
# # [print(element) for element in a if element < 5]
# # =============================================================================
# 
# a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# 
# # Random generated list:
# list_length = random.randint(5, 30)    # Length between 5 and 30, exclusive.
# random_list = list()
# 
# for element in range(5, list_length):
#     random_list.append(random.randint(5, 50))    # Generate random number between 5 and 50, exclusive,
#                                                  # to add to the list if even.
# 
# only_even_elements = [element for element in random_list if element%2 == 0]
# 
# print(only_even_elements)
# =============================================================================

# =============================================================================
# # Exercise 8: https://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html
# print("Choose between:\nRock: R, Paper: P, Scissors: S.")
# 
# gameOver = False
# while gameOver == False:
#     user1 = input("Player 1, chooses: ")
#     user2 = input("Player 2, chooses: ")
#     print("\n")
#     user1 = user1.upper()
#     user2 = user2.upper()
# 
#     if (user1 == 'R' and user2 == 'S') or (user1 == 'P' and user2 == 'R') or (user1 == 'S' and user2 == 'P'):
#         print("User 1 won!")
#     elif user1 == user2:
#         print("Draw...")
#     else:
#         print("User 2 won!")
# =============================================================================

# =============================================================================
# # Exercise 9: https://www.practicepython.org/exercise/2014/04/02/09-guessing-game-one.html
# 
# random_number = random.randint(0,10)
# count = 0
# user_input = None
# print("If you want to exit, type: exit")
# while user_input != random_number:
#     user_input = input("Enter a number: ").lower()
#     if user_input == 'exit':
#         sys.exit()
#         
#     user_input = int(user_input)
#     count += 1
#     if user_input > random_number:
#         print("Too high!")
#     elif user_input < random_number:
#         print("Too low!")
# 
# print(f"You guessed the number {random_number} correctly after {count} attemps.")
# print("Congrats!")
# =============================================================================

# =============================================================================
# # Exercise 10: https://www.practicepython.org/exercise/2014/04/10/10-list-overlap-comprehensions.html
# 
# ## First Approach: Known lists
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
#     [common_elements.append(element) for element in b_unique if element == i]
#     
#     # Not working. No idea why!
#     # common_elements = [element for element in b_unique if element == i]
# 
# print(f"List a is: {a_unique}")
# print(f"List b is: {b_unique}")
# print(f"List of common elements is: {common_elements}\n")
# 
# ## First approach but shorter:
#     
# result = [i for i in set(a) if i in b]
# print(f"Result: {result}" )
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
# common_elements2 = [element for element in set(a2) if element in b2]
# 
# # Sort final list
# a2.sort()
# b2.sort()
# common_elements2.sort()
# 
# print(f"List a is: {a2}")
# print(f"List b is: {b2}")
# print(f"List of common elements is: {common_elements2}")
# =============================================================================










