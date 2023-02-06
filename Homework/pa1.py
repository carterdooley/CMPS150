# Author: Type-Your-Name
# ULID: C004196163
# Course/Section: CMPS 150 – Lecture Section # 001
# Assignment: pa1
# Date Assigned: Monday, January 23, 2023
# Date/Time Due: Saturday, January 28, 2023 –- 11:59 pm
#
# Description: This program uses basic numeric operators to calculate the
# total cost for purchasing glazed donuts. The needed input is 
# provided by the user.
#
# Certification of Authenticity:
# I certify that this assignment is entirely my own work.



donuts = eval(input("Enter the number of donuts"))

if donuts >= 12:
    dozens = donuts // 12
    singles = donuts % 12
    costDozen = dozens * 9.95
    costSingle = singles * .95
    totalCost = costDozen + costSingle
    tax = totalCost * .0825
    totalCostTax = tax + totalCost
    
    costDozen = round(costDozen , 2)
    costSingle = round(costSingle , 2)
    tax = round(tax , 2)
    totalCost = round(totalCost , 2)
    totalCostTax = round(totalCostTax , 2)

    print("The price of the dozens of donuts before tax is", costDozen, "$ the cost of the singles before tax is", costSingle, 
          "$ The total cost before tax is", totalCost, "$")
    print("The tax is", tax, "$ The total after tax is", totalCostTax, "$")
else:
    donutsCost = donuts * .95
    tax = donutsCost * .0825
    donutsCostTax = donutsCost + tax


    donutsCost = round(donutsCost , 2)
    tax = round(tax, 2)
    donutsCostTax = round(donutsCostTax , 2)
    
    
    print("The price of the single donuts before tax was", donutsCost, "$ The tax is", tax, " $ The price of the single donuts after tax was", donutsCostTax, "$")