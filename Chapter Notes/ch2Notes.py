# Chapter 2 Notes January 25, 2023


# Divinding money into coin amounts
moneyAmount = eval(input("Please enter a amount of money in standard 0.00$ form"))

moneyAmount = moneyAmount * 100

quaters = moneyAmount // 25
leftoverMoney = moneyAmount % 25
dimes = leftoverMoney // 10
leftoverMoney = leftoverMoney % 10
nickles = leftoverMoney // 5
leftoverMoney = leftoverMoney % 5
pennies = leftoverMoney // 1




print(quaters, "quaters", dimes, "dimes", nickles, "nickles", pennies, "pennies")


#Shortcut operators
#Works as equal sign and math operator 


x = 0
print(x)
x += 8
print(x)
x -= 1
print(x)
x *= 2
print(x)
x/=2
print(x)
x %= 1
print(x)


