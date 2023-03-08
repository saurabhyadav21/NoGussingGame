# total = 0
# num = input("enter the value : ")
# for i in range (0,len(num)):
#     total += int(num[i])
# print(total)


# output>>>

# enter the value : 123
# 6

# >>>


# name = input("Please enter your name : ")
# temp = ""
# for i in range(len(name)):
#     if name[i] not in temp:
#         print(f"{name[i]} : {name.count(name[i])}")
#         temp += name[i]


# OUTPUT>>>


# Please enter your name : SAURABH YADAV
# S : 1
# A : 4
# U : 1
# R : 1
# B : 1
# H : 1
#   : 1
# Y : 1
# D : 1
# V : 1

# >>>




# guessing number game>>>>>>>>>>>>>>>>
 

# winning_number = 45
# guess = 1
# number = int(input("guess a number between 1 to 100 : "))
# game_over = False
# while not game_over:
#     if number == winning_number:
#         print(f"you win and you guessed this number in {guess} times ")
#         game_over = True
#     else:
#         if number < winning_number:
#             print("to low")
#             guess += 1
#             number = int(input("guess again : "))
#         else:
#             print("to high ")
#             guess += 1
#             number = int(input("guess again "))



# output>>>


# guess a number between 1 to 100 : 90
# to high 
# guess again 70
# to high 
# guess again 30
# to low
# guess again : 40
# to low
# guess again : 42
# to low
# guess again : 43
# to low
# guess again : 47
# to high 
# guess again 46
# to high 
# guess again 45
# you win and you guessed this number in 9 times 


# >>>


# with dry principal random number guessing game 

# import random
# winning_number = random.randint(1,100)
# guess = 1
# number = int(input("guess a number between 1 to 100 "))
# game_over = False
# while not game_over :
#     if number == winning_number :
#         print(f"you win and guessed this number in {guess} times ")
#         game_over = True
#     else:
#         if number < winning_number:
#             print("to low")
#         else:
#             print("to high")
#         guess += 1
#         number = int(input("guess again "))


# output>>>

# guess a number between 1 to 100 50
# to high
# guess again 40
# to high
# guess again 33
# to high
# guess again 32
# to high
# guess again 20
# to high
# guess again 10
# to high
# guess again 5
# to low
# guess again 6
# to low
# guess again 7
# you win and guessed this number in 9 times 

# >>>





