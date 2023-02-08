## Chapter 4 Notes
#If statements finally incorperated

import random as rdm

x = rdm.randint(0,9)
y = rdm.randint(0,9)

if x < y:
    x,y = y,x


answer = x - y


answerIn = eval(input("What is +str(x) Minus +str(y)"))

if answerIn == answer:
    print("correct")
else:
    print("incorrect")
    