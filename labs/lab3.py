import math
# lab3.py

# Author:        Your-Name
# ULID/Section:  Your-ULID & lecture section-number go here
 
 
# print 2 blank lines before the program begins

print('\n')

# ask the user for the radius of the pizza (in inches)  

pizzaRadius = eval(input("Enter the radius of the pizza in inches:"))
pizzaRadiusSQ = math.pi * (pizzaRadius ** 2)

# ask for the price of the pizza 

pizzaPrice = eval(input("Enter the price of the pizza: "))


# compute the price of the pizza per square inch

pricePerInch = pizzaPrice/pizzaRadiusSQ

# print the price NOT rounded

print("The price of the pizza exactly is:", pricePerInch)


# print the price rounded to 2 decimal places

pricePerInchRounded = round(pricePerInch, 2)

print(pricePerInchRounded)


# print 2 blank lines before the next section of code begins
# asking for input 
print('\n', '\n')

# ask the user to enter a 3-letter word 
# you are allowed only ONE input statement

word = input("Enter a 3-letter word: ")

# print the ASCII code (a number) for each letter of the word just input

print(word[0], ord(word[0]))
print(word[1], ord(word[1]))
print(word[2], ord(word[2]))


# print 2 blank lines when the program is done
print('\n','\n')

