# import math

# #Chapter 1 Intro To Python and Python basics

# #Variables are defined very simply
# #EX:

# x = 1
# y = 2

# name  = "carter"

# breathing = True


# print(x,y,name,breathing, "Why are we still learning print statements")

# #Defining Functions :
# #Functions are defined using the word def at the beggining:
# #Ex:

# def print_the_answer(x,y) :
#     final_answer = x + y
#     print(x+y)
#     return final_answer

# #if statements

# def if_breathing (is_breathing) :
#     if is_breathing == True :
#         print("Yes I am breathing")
#         return True

# #Loops
# loop_length = 1

# while loop_length <= 10 :
#     print("Hello")
#     loop_length = loop_length + 1

# #Loops and "if" statement combination
# #Always recheck the loop iteration to ensure no infinite loop is created
# while loop_length <= 100 :
#     if loop_length % 2 == 0:
#         print("bob")
#     else :
#         print("ross")
#     loop_length = loop_length + 1



# xy = math.pi * x * y
# print(xy)


# # Inputs

# myName = input("Enter your name: ")
# print (myName)



# # Arrays, Array List, and List:

# friends = ['Joe', 'Sally', 'Camilo', 'Perry', 'Susan']

# friends.append('Carter')

# print(len(friends))

# friends.insert(2, "John")
# print(friends)

# friends.pop()
# print(friends)


# #Second Array Example :
# numbers = [1,2,3,4,5,6,7,8,9,10]


# for number in numbers:
#     print(number)

# even_numbers = []

# for number in numbers:
#     if number % 2 == 0:
#         even_numbers.append(number)
        
# print(even_numbers)

# score = 74

# if score >= 90:
#     print('A')
# elif score >= 80: 
#     print('B')
# elif score >= 70:
#     print('C')
# elif score >= 60:
#     print('D')
# else:
#     print('F')






# Lab 1 Related Code:


name = input("Enter your name")
age =  input("Enter your age")
print("Hi my name is", name, "And I am", age, "years old")