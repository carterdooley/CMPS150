import math


#Chapter 1 Intro To Python and Python basics

#Variables are defined very simply
#EX:

x = 0
y = 2

name  = "carter"

breathing = True

#Defining Functions :
#Functions are defined using the word def at the beggining:
#Ex:

def print_the_answer(x,y) :
    final_answer = x + y
    print(x+y)
    return final_answer

#if statements

def if_breathing (is_breathing) :
    if is_breathing == True :
        print("Yes I am breathing")
        return True

#Loops
loop_length = 1

while loop_length <= 10 :
    print("Hello")
    loop_length = loop_length + 1

#Loops and if statement combination
while loop_length <= 100 :
    if loop_length % 2 == 0:
        print("bob")
    else :
        print("ross")
    loop_length = loop_length + 1



xy = math.atan(15)

print(xy)

